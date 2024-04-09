from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
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
    variance = #closest integer
    
    #sort all buy orders and sell orders to recognize best ask and best bid
    #calculate midpoint
    
    #try to buy slightly above 
    
    
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
      traderData = "SAMPLE" 
      
      # Sample conversion request. Check more details below. 
      conversions = 1
      return result, conversions, traderData