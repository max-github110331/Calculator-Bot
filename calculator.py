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
        try:
            ans=str(eval(self.calcu))
        except:
            ans="ERROR!"
        if ans.endswith(".0"):
            return ans[:-2]
        else:
            return ans
