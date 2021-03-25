from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self):
        super().__init__('Agent를 찾을 수 없습니다.')


class Agent(object):
    """
    1명당 최대 load는 3
    """
    MAX_LOAD = 3

    def __init__(self, name, skills, load):
        self._name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)

    def check_load(self):
        return self.load < self.MAX_LOAD


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    """
    agent load 값이 3개 미만인지 체크
    agent skills에 Ticket 값에 포함되어 있는지 체크
    """
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        """
        agent load 값이 3개 미만인지 체크
        """
        agents = [agent for agent in agents if agent.check_load()]
        if agents:
            return agents
        raise NoAgentFoundException

    def find(self, ticket: Ticket, agents: List[Agent]) -> List[Agent]:
        """
        agent skills에 Ticket 값에 포함되어 있는지 체크
        """
        new_agents = []
        agents = self._filter_loaded_agents(agents)
        if agents:
            for agent in agents:
                if any(skill in agent.skills for skill in ticket.restrictions):
                    new_agents.append(agent)
        if new_agents:
            return new_agents
        raise NoAgentFoundException


class LeastLoadedAgent(FinderPolicy):
    """
    load 값이 가장 적은 Agent 찾기
    """
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        new_agents = super().find(ticket, agents)
        return min(new_agents, key=lambda x: x.load)


class LeastFlexibleAgent(FinderPolicy):
    """
    사용가능하면서(load 3이하, Skills 포함), Skills가 가장 적은 Agent 찾기
    """

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        new_agents = super().find(ticket, agents)
        return min(new_agents, key=lambda x: len(x.skills))


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
print(least_loaded_policy.find(ticket, [agent1, agent2]))

least_flexible_policy = LeastFlexibleAgent()
print(least_flexible_policy.find(ticket, [agent1, agent2]))
