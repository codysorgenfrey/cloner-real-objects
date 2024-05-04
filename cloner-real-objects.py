import c4d
from c4d.modules import mograph as mo

doc: c4d.documents.BaseDocument  # The document containing this field object.
op: c4d.BaseTag # The Python tag containing this code.
flags: int # The execution flags of `main()`. See c4d.EXECUTIONFLAGS for details.
priority: int # The execution priority of this tag. See c4d.EXECUTIONPRIORITY for details.
tp: c4d.modules.thinkingparticles.TP_MasterSystem # The TP system of the document.

def main() -> None:
    obj = op.GetObject()
    cloner = op[c4d.ID_USERDATA,1] # link to cloner object

    md = mo.GeGetMoData(cloner)
    if (md is None):
        return

    marr = md.GetArray(c4d.MODATA_MATRIX)
    child = obj.GetDown()
    i = 0

    while (child):
        child.SetMg(marr[i])
        child.Message(c4d.MSG_UPDATE)
        i = i + 1
        child = child.GetNext()

    c4d.EventAdd() # not sure if needed