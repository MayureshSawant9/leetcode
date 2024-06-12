class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_count = collections.defaultdict(int)
        all_players = set()

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            loser_count[loser] += 1

        zero_loss = []
        one_loss = []

        for player in all_players:
            if loser_count[player] == 0:
                zero_loss.append(player)
            elif loser_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]