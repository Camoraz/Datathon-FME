
class FormData:
    def __init__(self, years, role, challenge, lang, level, age, hackathons) -> None:
        self.years= self.formatYears(years)
        self.role = self.formatRole(role)
        self.challenge = self.formatChallenge(challenge)
        self.lang = self.formatLang(lang)
        self.level = self.formatLevel(level)
        self.age = self.formatAge(age)
        self.hackathons = self.formatHackathons(hackathons)
    
    def formatYears(self, years):
        years = years.lower().strip()
        if years in ['1', '2', '3', '4', 'master', 'phd']:
            return int(years)
        return None
    def formatRole(self, role):
        role = role.lower().strip()
        if role in ['analysis', 'visualization', 'development', 'design']:
            return role
        return None
    def formatChallenge(self, challenge):
        for i, c in enumerate(challenge):
            challenge[i] = c.lower().strip()
        if challenge in ['restb.ai challenge', 'aed challenge', 'mango challenge']:
            return challenge
        return None
    def formatLang(self, lang):
        for i,l in enumerate(lang):
            lang[i] = l.lower().strip()
        return lang
    def formatAge(self, age):

        age = age.lower().strip()
        if age.isnumeric():
            return int(age)
        return None
    def formatLevel(self, level):
        level = level.lower().strip()
        if level in ['beginner', 'intermediate', 'advanced']:
            return level
        return None
    def formatHackathons(self, hackathons):
        hackathons = hackathons.lower().strip()
        if hackathons.isnumeric():
            return int(hackathons)
        return None

    