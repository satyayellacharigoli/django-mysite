from student.views import BranchViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('branch',BranchViewSets)

