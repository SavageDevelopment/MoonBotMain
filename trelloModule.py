from trello import TrelloClient

key = 'f007d04dea6c81916d62e97d7b27a554'
token = 'dc32d25088855a71cda7a7e55e3defd36422cdf84c31ee05d846b93306003b95'
trello = TrelloClient(key, token)

def trllo_SendCode(rbxUser, userid):
  BOARD_ID = "61baf09d324a9c480602ede3"
  LIST_ID = "61baf0ae9082373dd8958ad6"

  board = trello.get_board(BOARD_ID)
  target_list = board.get_list(LIST_ID)
  target_list.add_card(rbxUser,userid)

def trello_cleanUp(key):
  mainCard = trello.get_card(key)
  return(mainCard.description)

def getRbx_Username(key):
  mainCard = trello.get_card(key)
  return(mainCard.name)
