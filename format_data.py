
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
        years = years.strip()
        if years in ['1st year', '2nd year', '3rd year', '4th year', 'Master', 'PhD']:
            return years
        return None
    def formatRole(self, role):
        role = role.strip()
        if role in ['Analysis', 'Visualization', 'Development', 'Design']:
            return [role]
        return None
    def formatChallenge(self, challenge):
        l = []
        for c in challenge:
            match(c):
                case 'restb.ai challenge':
                    l.append('restb.ai challenge')
                    break
                case 'aed challenge':
                    l.append('aed challenge')
                    break
                case 'mango challenge':
                    l.append('mango challenge')
        return l
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
        level = level.strip()
        if level in ['Beginner', 'Intermediate', 'Advanced']:
            return level
        return None
    def formatHackathons(self, hackathons):
        hackathons = hackathons.lower().strip()
        if hackathons.isnumeric():
            return int(hackathons)
        return None

    