import gym
import numpy as np

class RiverCrossing(gym.Env):
    """
    2D river crossing environment. The agent (a boat, modelled as a point mass which experiences drag force due to the water flow) must traverse a river (which has a specified flow field). To reach a specific point on the other side of the river.


    TODO The flow may be specified such that the boat cannot reach the goal without hitting obstacles downstream. In this case, the best strategy for the agent will be to return to the original point of departure (for the duration of that episode).


    The idea is to develop an AI that can solve this problem while using highly abstracted models of the environment.

    This is different from multigrid in several important ways:
        - The state is continuous
            - At least within the environment, the agent may only have access to a simplified version of the "true" state in its observations

        - The action space is continuous
            - The two "input" variables variables I want for the agent are:
                - the rate of change of heading (constrained by a max value)
                - forward velocity (constrained by a max value)
                - of course, if I'm doing a "simplified" agent, I want to only give the agent access to extremely simplified versions of these readings
                    - could the process of "simplifying" be captured in a clean function? Something like the "observation" matrix C from linear control theory, but it "simplifies" information to a point where it is simple enough for a human to make decisions on it.

        - It uses vectors for position and forces and all that stuff
            - Let's define our coordinate basis

                \hat{x} is the downstream direction. x=0 is the center of the screen.
                \hat{y} is the "accoss stream" direction. y=0 is the center of the river (a convenient choice to define flow field which is symmetric about the center of the river). The boat starts from the bottom shore of the river and moves in the +y direction to reach the other shore

             \hat{y}
                ^
                |
                |
                |
                -------> \hat{x}


        - There are external forces from water drag that will influence the agent position even if no action is taken.
            - This means I need a way to model the forces from the fluid
                https://en.wikipedia.org/wiki/Drag_(physics)
                F_D = 0.5 * rho * v**2 * C_D * A
                    - F_D: drag force [kg * m / s^2]
                    - rho: fluid density in kg / m^3
                    - v: relative velocity between fluid and the body (v is a scalar, but you calculate it using vector quantities)
                    - C_D: drag coefficient of the body
                    - A: cross-sectional area of the body


            - For a first cut, we'll assume a parabolic velocity profile.
                - u(y) = (1 - ((2y)/h)^2 ) u_max \hat{x}
                    - fluid velocity equation
                    - u_max is the max velocity (which I specifiy) at the center of the river

                - Also assume the agent does not affect the flow of the fluid (reasonable for small watercraft in larger bodies of water), and we'll abstract away from flow (in the environment model) to just consider fluid as a position and velocity-dependent force.

            - For the purposes of external forces (only drag forces), we model the agent as a sphere with a 1 meter radius
                - This gives:
                    - C_D = 0.5 (drag coefficient, dimensionless)
                    - A = pi * r **2

    """

    def __init__(self):
        # initialize any values needed for the environment
        pass


    def reset(self):
        pass


    def step(self):
        pass


    def render(self):
        pass

    def _fluid_velocity(self, y_pos, fluid_velocity_field="parabolic"):
        if fluid_velocity_field == "parabolic":
            # max fluid velocity in the center of the river
            self.u_max = 1 # m/s
            u_fluid = (1 - ((2 * y_pos) / self.h) ** 2) * self.u_max
            return np.array([0, u_fluid])


        pass

    def _calculate_forces_on_agent(self):
        pass
