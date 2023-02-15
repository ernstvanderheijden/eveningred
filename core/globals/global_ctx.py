from core.globals.global_functions import create_ctx_slug
from pydoc import locate
from shared.menumodules import lefttop, leftbottom


class ChapterCtxData:
    def __init__(self, request, viewtype, *args, **kwargs):
        super(ChapterCtxData, self).__init__(*args, **kwargs)
        """Load menu's"""
        self.lefttopmenu = lefttop.set_moduledata(request)   # Loading the menu
        self.leftbottommenu = leftbottom.set_moduledata(request)   # Loading the menu
        self.viewtype = viewtype

        """Get variables from request"""
        self.level = request.GET.get('level', 0)
        self.package = request.GET.get('package', '')
        self.chapter = request.GET.get('chapter', '')
        self.pk = request.GET.get('pk', '')
        self.templatename = "core/chapter/chapter.html"


def create_chapterctxdata(request, viewtype=None, pk=None):
    ctx = vars(ChapterCtxData(request, viewtype))
    """Fill ctx with variables from a module"""
    if request.GET.get("package", ''):
        package = request.GET.get('package', '')
        fk = request.GET.get('fk', None)
        chapter = request.GET.get('chapter', '')
        crud = request.GET.get('crud', '')
        if not pk:
            pk = request.GET.get('pk', None)
        if viewtype == 'create' or viewtype == 'update' or viewtype == 'delete':
            modulepath = "shared.packages." + package.lower() + "." + crud.lower()
            nameclass = getattr(locate(modulepath), crud.title())
        else:
            modulepath = "shared.packages." + package.lower() + ".chapters." + chapter.lower()
            nameclass = getattr(locate(modulepath), chapter.title())
        ctx.update(vars(nameclass(request, viewtype, pk)))
        ctx.update({"html_header": "core/modals/modalheader.html"})
        ctx.update({"html_footer": "core/modals/modalfooter.html"})
    ctx = create_ctx_slug(ctx)
    return ctx
