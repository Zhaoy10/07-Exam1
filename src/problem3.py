"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and YiqiZhao.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem3  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(10, 20), 200, 25, window)
    window.close_on_mouse_click()

    # TWO tests on ONE window.
    title = 'Tests 2, 3 and 4 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(15, 30), 100, 20, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 10), 90, 45, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 125), 80, 45, window)
    window.close_on_mouse_click()


def problem3(point, length, delta, window):
    l=length
    d=delta
    gg=rg.Point(point.x,length+point.y)
    G =rg.Line(point,gg)
    G.thickness=3
    G.color='black'
    G.attach_to(window)
    window.render()
    for k in range((l//delta)+1):
        ls=rg.Line(point,rg.Point(point.x+length,point.y))
        point.y=point.y+d
        ls.thickness=3
        l=l+20
        if k%3 ==0:
            ls.color='megenta'
        if k% 3==1:
            ls.color='cyan'
        if k% 3 == 2:
            ls.color='spring green'

        ls.attach_to(window)
    window.render()

    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- Two positive integers
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given rg.RoseWindow:

      -- A VERTICAL rg.Line for which:
           -- Its topmost point is the given point.
           -- Its length is the given length.
           -- Its color is 'black'.
           -- Its thickness is 3.

      -- Several HORIZONTAL rg.Lines such that:
           -- All the horizontal lines have their leftmost point
                on the vertical line.  SEE THE PICTURES.
           -- For the FIRST of these HORIZONTAL lines:
                -- Its leftmost point is the given point.
                -- Its length is the given length.
           -- Each SUBSEQUENT HORIZONTAL rg.Line is  delta  pixels
                directly below the previous rg.Line (where delta is a parameter)
                and 20 pixels longer than the previous rg.Line.
           -- All the HORIZONTAL lines have thickness 3.
           -- The 1st, 4th, 7th, etc rg.Lines have color 'magenta',
              The 2nd, 5th, 8th, etc rg.Lines have color 'cyan'
              The 3rd, 6th, 9th, etc rg.Lines have color 'spring green'

      NOTE: The NUMBER of lines to draw is determined by the facts that:
        -- The vertical line has the given length.
        -- All horizontal lines have their left endpoint on the vertical line.
        -- The distance between horizontal lines is the given delta.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:   rg.Point
      :type length:  int
      :type delta:   int
      :type window:  rg.RoseWindow
    """
    # --------------------------------------------------------------------------
    # : 2. Implement and test this function.
    #  (continued):  IMPORTANT: Use this ITERATIVE ENHANCEMENT PLAN:
    #  (continued):    1. Make the sole VERTICAL line appear,
    #  (continued):         with thickness 3.
    #  (continued):    2. Make the FIRST horizontal line appear.
    #  (continued):    3. Make MORE horizontal lines appear,
    #  (continued):         each delta below the previous one.
    #  (continued):    4. Make each successive horizontal line
    #  (continued):         20 pixels longer than the previous one.
    #  (continued):    5. Make the right NUMBER of horizontal lines.
    #  (continued):    6. Make the horizontal lines each have thickness 3
    #  (continued):         and colors per the specified pattern.
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
