import pandas as pd

#returns the res array with [numbers of rows, number of columns]
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    res = [len(players.axes[0]), len(players.axes[1])]
    return res