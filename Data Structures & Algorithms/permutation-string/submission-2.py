class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # two dicts
        ds1 = defaultdict(int)
        ds2 = defaultdict(int)

        for s in s1:
            ds1[s] += 1
        
        # now we need to trsvel through s2 at window length of s1
        # so we create a dict of size s1 FOR s2
        # but we travel, add and remove element in the dict

        for i in range(len(s1)): # len s1 here as we need the travel dict to be of len s1
            ds2[s2[i]] += 1
        
        '''
            till here we have 2 dicts, ds1 and dsd2
            if s1 = abc, and s2 = lebac

            then    ds1 = {a:1, b:1, c:1}
                    ds2 = {l:1, e:1, b:1}
        '''

        '''
            now that we have both dicts we check if they're the same
            I mean if s1 = abc and s2 = cab
            then, we would have had same dict
        '''
        if ds1 == ds2:
            return True
        
        # Code comes here when ds1 != ds1
        '''
            Now that we know both dicts are not same
            take s1 = abc, and s2 = lebac
            ds1 = a,b,c all 1
            ds2 = leb with 1
            since we compared abc to leb earlier with false result
                we now need to compare 'abc' next word window
                    abc == eba
                    we do this by adding a from s2 (lebac) to ds2
                    and removing l from ds2

                    we then check if ds1 == ds2, if true we retunr
                    else, we continue adding and removing to ds2
        '''
        for i in range(len(s1), len(s2)):
            # for loop here ranges from len of s1 to len of s2 
            # cuz we are manipulating ds2 dict
            # and ds2 already has size of 3 (len s1)
            # ( we need to keep that size )
            # first 3 elements are already in ds2,
            # we now loop through elemnts after first 3
            ds2[s2[i]] += 1
            ds2[s2[i - len(s1)]] -= 1

            if ds2[s2[i - len(s1)]] == 0:
                del ds2[s2[i - len(s1)]]
                
            if ds1 == ds2:
                return True

        return False
