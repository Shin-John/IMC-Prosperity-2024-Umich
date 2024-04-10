from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import collections
from collections import defaultdict
import pandas
import string

#update as we progress into further rounds
empty_dict = {'AMETHYST' : 0, 'STARFRUIT' : 0}

INF = int(1e9)

class Trader:
  
  POSITION_LIMIT = {'AMETHYST' : 20, 'STARFRUIT' : 20}
  
  #code from the tutorial algo
  # def tutorialAlgo():
  #   if len(order_depth.sell_orders) != 0:
  #     best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
  #     if int(best_ask) < acceptable_price:
  #         print("BUY", str(-best_ask_amount) + "x", best_ask)
  #         orders.append(Order(product, best_ask, -best_ask_amount))
  
  #   if len(order_depth.buy_orders) != 0:
  #     best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
  #     if int(best_bid) > acceptable_price:
  #         print("SELL", str(best_bid_amount) + "x", best_bid)
  #         orders.append(Order(product, best_bid, -best_bid_amount))
  
  def compute_amethyst(self, order_depth, timestamp, ):
    orders: list[Order] = []
    
    #our current position on the product
    cpos = self.position['AMETHYST']
    #determine mean and avg variance 
    acc_bid_and_ask = 10000
    
    #sort all buy orders and sell orders to recognize best ask and best bid
    osell = collections.OrderedDict(sorted(order_depth.sell_orders.items()))
    obuy = collections.OrderedDict(sorted(order_depth.buy_orders.items(), reverse=True))

    sell_vol, best_sell_pr = self.values_extract(osell)
    buy_vol, best_buy_pr = self.values_extract(obuy, 1)
    
    for ask, vol in osell.items():
      if ((ask < 10000) or ((self.position['AMETHYST']<0) and (ask == 10000))) and cpos < self.POSITION_LIMIT['AMETHYST']:
        order_for = min(-vol, self.POSITION_LIMIT['AMETHYST'] - cpos)
        cpos += order_for
        assert(order_for >= 0)
        orders.append(Order('AMETHYST', ask, order_for))
    
    undercut_buy = best_buy_pr + 1
    undercut_sell = best_sell_pr - 1
    
    bid_pr = min(undercut_buy, 10000-1) # we will shift this by 1 to beat this price
    sell_pr = max(undercut_sell, 10000+1)
    
    for bid, vol in obuy.items():
      if ((bid > 10000) or ((self.position['AMETHYST']>0) and (bid == 10000))) and cpos > -self.POSITION_LIMIT['AMETHYST']:
        order_for = max(-vol, -self.POSITION_LIMIT['AMETHYST']-cpos)
        cpos += order_for
        assert(order_for <= 0)
        orders.append(Order('AMETHYST', bid, order_for))
          
    return orders
    

    
    
  def run(self, state: TradingState):
    #print("traderData: " + state.traderData)
    #print("Observations: " + str(state.observations))

    # Orders to be placed on exchange matching engine
    result = {'AMETHYST' : [], 'STARFRUIT' : []}
    
    current_position = {'AMETHYST' : 0, 'STARFRUIT' : 0}
    
    #scan and print our current position based on each product
    for key, val in state.position.items():
      self.position[key] = val
    for key, val in self.position.items():
      print(f'{key} position: {val}')
      
    #get current timestamp
    timestamp = state.timestamp
    
    order = self.compute_amethyst(state.order_depths, state.timestamp)
    result['AMETHYST'] += order
    
    
    
    
    
    
    #ignore this segment of code for now, this is tutorial code
    # for product in state.order_depths:
    #     order_depth: OrderDepth = state.order_depths[product]
    #     orders: List[Order] = []
    #     acceptable_price = 10  # Participant should calculate this value
    #     print("Acceptable price : " + str(acceptable_price))
    #     print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))

        
        
    #     result[product] = orders

    # String value holding Trader state data required. 
    # It will be delivered as TradingState.traderData on next execution.
    traderData = "" 
    
    # Sample conversion request. Check more details below. 
    conversions = 0
    return result, conversions, traderData