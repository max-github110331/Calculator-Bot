class Calculator:
    def __init__(self):
        self.calcu=""


    async def appead(self, num: str):
        self.calcu=f"{self.calcu}{num}"
        return self.calcu


    async def delete(self):
        self.calcu=f"{self.calcu[:-1]}"
        return self.calcu


    async def equal_to(self):
        return str(eval(self.calcu))