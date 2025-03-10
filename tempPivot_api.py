import maya.api.OpenMaya as om
import maya.cmds as cmds

# 전역 변수로 콜백 ID 저장
callback_id = None

# 프레임 변경 이벤트 핸들러
def on_frame_changed(*args):
    if cmds.objExists("pCube1"):
        selection_list = om.MSelectionList()
        selection_list.add("pCube1")
        dag_path = selection_list.getDagPath(0)
        transform_fn = om.MFnTransform(dag_path)

        position = transform_fn.translation(om.MSpace.kWorld)
        print(f"Frame {cmds.currentTime(q=True)}: Cube Position: {position}")
    else:
        print("Cube not found!")

# 콜백 등록 함수
def register_callback():
    global callback_id
    if callback_id is None:  # 중복 등록 방지
        callback_id = om.MEventMessage.addEventCallback("timeChanged", on_frame_changed)
        print("Frame change callback registered!")

# 콜백 제거 함수
def remove_callback():
    global callback_id
    if callback_id is not None:
        om.MMessage.removeCallback(callback_id)
        print("Frame change callback removed!")
        callback_id = None  # ID 초기화

# 초기 등록
register_callback()

#remove_callback()