#What's the angle between clock faces when it's 3:15?
#Write a  function that returns angle between clock faces for any (hour, minute).
def clock_face(hour, minute):

    #we use 12 oclock as reference.each min is 6 degree 360/60 every hour is 360/12 = 30 + (angel of each hour /60  30/60 = 0.5)
    angel = ( hour * 30 + minute * 0.5 ) - ( minute * 6 )
    return abs(angel)


print(clock_face(3,45))
