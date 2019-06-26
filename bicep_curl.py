
import numpy as np
def bicep_curl(pose):
    right_present = 0
    left_present = 0
    for part in pose:
        if str(part.get_part_name()).split('.')[1] == "RShoulder":
            right_present+=1
        elif str(part.get_part_name()).split('.')[1] == "RElbow":
            right_present +=1 
        elif str(part.get_part_name()).split('.')[1] == "RWrist":
            right_present += 1 
        elif str(part.get_part_name()).split('.')[1] == "LShoulder":
            left_present += 1
        elif str(part.get_part_name()).split('.')[1] == "LElbow":
            left_present += 1 
        elif str(part.get_part_name()).split('.')[1] == "LWrist":
            left_present += 1
    side = 'right' if right_present > left_present else 'left'
    print(right_present)
    print(left_present)
    print('Exercise arm detected as: {}.'.format(side))
    
    if side == 'right':
        pose_dict = {}
        for part in pose:
            bp = str(part.get_part_name()).split('.')[1]
            if bp == "RShoulder":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "RElbow":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "RWrist":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "RHip":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "Neck":
                pose_dict[bp] = (part.x, part.y)
    else:
        pose_dict = {}
        for part in pose:
            bp = str(part.get_part_name()).split('.')[1]
            if bp == "LShoulder":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "LElbow":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "LWrist":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "LHip":
                pose_dict[bp] = (part.x, part.y)
            elif bp == "Neck":
                pose_dict[bp] = (part.x, part.y)
    print(pose_dict)
    print(len(pose_dict))
    if len(pose_dict) == 5:
        upper_arm_vecs = np.array([pose_dict["LShoulder"][0] - pose_dict["LElbow"][0], pose_dict["LShoulder"][1] - pose_dict["LElbow"][1]])
        torso_vecs = np.array([pose_dict["Neck"][0] - pose_dict["LHip"][0], pose_dict["Neck"][1] - pose_dict["LHip"][1]])
        forearm_vecs = np.array([pose_dict["LWrist"][0] - pose_dict["LElbow"][0], pose_dict["LWrist"][1] - pose_dict["LElbow"][1]])
        
    # normalize vectors
        upper_arm_vecs = upper_arm_vecs / (np.linalg.norm(upper_arm_vecs))
        torso_vecs = torso_vecs /(np.linalg.norm(torso_vecs))
        forearm_vecs = forearm_vecs / (np.linalg.norm(forearm_vecs))
        
        upper_arm_torso_angles = np.degrees(np.arccos(np.clip(np.dot(upper_arm_vecs, torso_vecs), -1.0, 1.0)))
        upper_arm_forearm_angles = np.degrees(np.arccos(np.clip(np.dot(upper_arm_vecs, forearm_vecs), -1.0, 1.0)))
        
        print(upper_arm_torso_angles)
        print(upper_arm_forearm_angles)
        result = (upper_arm_torso_angles, upper_arm_forearm_angles)
    else:
        result = "all keypoints are not visible"
    
    return result, side
# =============================================================================
#         joints = [(pose.rshoulder, pose.relbow, pose.rwrist, pose.rhip, pose.neck) ]
#     else:
#         joints = [(pose.lshoulder, pose.lelbow, pose.lwrist, pose.lhip, pose.neck) for pose in poses]
# =============================================================================
# =============================================================================
#     if side == 'right':
#         joints = [(CocoPart.RShoulder, CocoPart.RElbow, CocoPart.RWrist, CocoPart.RHip, Cocopart.Neck) for part in pose]
#     else:
#         joints = [(CocoPart.LShoulder, CocoPart.LElbow, CocoPart.LWrist, CocoPart.LHip, Cocopart.Neck) for part in pose]
# =============================================================================

#     pose_name = list(pose_keypoints.keys())
#     right_present = 0
#     left_present = 0
#     
#     for pose in pose_name:
#         if pose == 2:
#             right_present += 1
#         elif pose == 3:
#             right_present += 1
#         elif pose == 4:
#             right_present += 1
#         elif pose == 5:
#             left_present += 1
#         elif pose == 6:
#             left_present += 1
#         elif pose == 7:
#             left_present += 1
#     
# # =============================================================================
# #     right_count = sum(right_present)
# #     left_count = sum(left_present)
# # =============================================================================
#     
#     side = 'right' if right_present > left_present else 'left'
# # =============================================================================
# #     return side
# # =============================================================================
#     joints = []
#     if side == 'right':
#         for i in pose_keypoints:
#             if i == "2":
#                 joints.append(pose_keypoints[i])
#             if i == "3":
#                 joints.append(pose_keypoints[i])
#             if i == "4":
#                 joints.append(pose_keypoints[i])
#                 
#     else:
#         for i in pose_keypoints:
#             if i == "5":
#                 joints.append(pose_keypoints[i])
#             if i == "6":
#                 joints.append(pose_keypoints[i])
#             if i == "7":
#                 joints.append(pose_keypoints[i])
#     #print('Exercise arm detected as: {}.'.format(side))
#     
#     upper_arm_vecs = np.array([(joint[0].x - joint[1].x, joint[0].y - joint[1].y) for joint in joints])
#     torso_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
#     forearm_vecs = np.array([(joint[2].x - joint[1].x, joint[2].y - joint[1].y) for joint in joints])
#     
#     # normalize vectors
#     upper_arm_vecs = upper_arm_vecs / (np.linalg.norm(upper_arm_vecs))
#     torso_vecs = torso_vecs /(np.linalg.norm(torso_vecs))
#     forearm_vecs = forearm_vecs / (np.linalg.norm(forearm_vecs))
#     
#     upper_arm_torso_angles = np.degrees(np.arccos(np.clip(np.multiply(upper_arm_vecs, torso_vecs), -1.0, 1.0)))
#     upper_arm_forearm_angles = np.degrees(np.arccos(np.clip(np.multiply(upper_arm_vecs, forearm_vecs), -1.0, 1.0)))
#     
#         # use thresholds learned from analysis
# # =============================================================================
# #     upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
# #     upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
# # =============================================================================
# 
#     print('Upper arm and torso angle range: {}'.format(upper_arm_torso_angles))
#     print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_angles))
#     
# # =============================================================================
# #     correct = True
# #     feedback = ''
# # 
# #     if upper_arm_torso_range > 35.0:
# #         correct = False
# #         feedback += 'Your upper arm shows significant rotation around the shoulder when curling. Try holding your upper arm still, parallel to your chest, ' + \
# #                     'and concentrate on rotating around your elbow only.\n'
# #     
# #     if upper_arm_forearm_min > 70.0:
# #         correct = False
# #         feedback += 'You are not curling the weight all the way to the top, up to your shoulders. Try to curl your arm completely so that your forearm is parallel with your torso. It may help to use lighter weight.\n'
# # 
# #     if correct:
# #         return (correct, 'Exercise performed correctly! Weight was lifted fully up, and upper arm did not move significantly.')
# #     else:
# #         return (correct, feedback)
# # =============================================================================
#     return upper_arm_torso_angles,upper_arm_forearm_angles
# =============================================================================
