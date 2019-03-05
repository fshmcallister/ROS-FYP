import rospy
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    return TriggerResponse(
        success = True
        message = "Successful"
    
    )
rospy.init_node('sos_service')
my_service = rospy.Service('/fake_911', Trigger, trigger_response)
rospy.spin()

#taken from tutorial