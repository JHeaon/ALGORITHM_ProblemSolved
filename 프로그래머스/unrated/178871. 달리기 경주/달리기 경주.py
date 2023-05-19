from typing import List, Dict

def solution(players, callings) -> List[str]:
    
    players_rank_dict: Dict[str, int] = {players: rank + 1 for rank, players in enumerate(players)}
    rank_players_dict: Dict[int, str] = {rank + 1: players for rank, players in enumerate(players)}
    
    for calling in callings:
        player1_rank = players_rank_dict[calling]
        player1_name = calling
        
        player2_rank = players_rank_dict[rank_players_dict[player1_rank - 1]]
        player2_name = rank_players_dict[player2_rank]
        
        players_rank_dict[player1_name] -= 1
        players_rank_dict[player2_name] += 1
        
        rank_players_dict[player1_rank] = player2_name
        rank_players_dict[player2_rank] = player1_name
        
        
    answer = [player for player, rank in sorted(players_rank_dict.items(), key=lambda x: x[1])]
        
    return answer


