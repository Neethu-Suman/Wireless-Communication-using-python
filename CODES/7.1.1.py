import simpy
class AODV(object):
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.action = env.process(self.run())

    def run(self):
        while True:
            # Routing table update process
            yield self.env.timeout(1)
            print("Updating routing table at time {}".format(self.env.now))

            # Route discovery process
            yield self.env.timeout(2)
            print("Starting route discovery at time {}".format(self.env.now))

            # Sending data packets
            yield self.env.timeout(1)
            print("Sending data packets at time {}".format(self.env.now))
# Create the simulation environment
env = simpy.Environment()
# Start the AODV process
aodv = AODV(env)
# Run the simulation
env.run(until=10)