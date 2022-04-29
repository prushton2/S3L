class S3LExpression:
    def __init__(self, select, from_, where, extendedChars):
        self.select = select
        self.from_ = from_
        self.where = where
        self.extendedChars = extendedChars

    def __str__(self):
        string = ""
        for index, char in enumerate(self.from_):
            printed = False

            for eIndex, eChar in enumerate(self.extendedChars):
                if(eChar[0] <= index <= eChar[1]):
                    if(not printed):
                        string += '\033[4m' + char + '\033[0m'
                        printed = True

            if(not printed):
                string += char
        return string