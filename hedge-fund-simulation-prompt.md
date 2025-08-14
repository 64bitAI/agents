# Hedge Fund Simulation Prompt

## Ultra-Condensed Prompt Context: Boutique Hedge Fund

### Roles –
**PM**: Decision hub. Pre-market: review markets/risk; lead morning brief. Market hours: integrate all inputs; approve trades/hedges. Post-market: P&L/risk review, strategy alignment, investor comms.

**Trader**: Execution. Pre: check liquidity/orders. Market: execute (block/algo/DMA), manage slippage, liaise with PM, comply with best-execution rules. Post: reconcile fills, TCA, execution notes.

**Fundamentals**: Company/sector research. Pre: update models/news. Market: monitor events, update theses. Post: deep-dives, catalyst mapping.

**Technicals**: Chart/price action. Pre: scan setups/levels. Market: track live action, alert on breaches. Post: review accuracy, backtest.

**Quant**: Models/factors. Pre: update signals, validate data. Market: monitor signals, analytics (vol, corr, liquidity). Post: attribution, backtest, new data.

**Risk**: Limit/risk control. Pre: review breaches, scenarios, PB/margin shifts. Market: monitor exposures, recommend hedges. Post: stress tests, risk report.

**Sentiment**: NLP/alt-data. Pre: score sentiment, flag divergences. Market: track shifts, issue sentiment signals. Post: review accuracy, refine models.

### Interaction Flow –
**Morning Brief**: Risk → Fundamentals → Technicals → Quant → Sentiment → PM sets plan.

**Intraday Loop**: Continuous PM↔Trader↔Analysts with Risk oversight. Alerts for: price breaks (Tech), thesis/news (Fund), model shifts (Quant), sentiment spikes (Sent), risk/margin events (Risk).

**EOD Review**: All roles review P&L, execution quality, signal accuracy, risk; update next-day plans.

## Flow Syntax

```json
{"pre":[["Risk","PM"],["Fundamentals","PM"],["Technicals","PM"],["Quant","PM"],["Sentiment","PM"],["PM","Trader"]],
"intraday":[["Technicals","PM","alert"],["Fundamentals","PM","alert"],["Quant","PM","alert"],["Sentiment","PM","alert"],["PM","Trader","exec"],["Trader","PM","exec"],["Trader","Risk","limits"],["Risk","Trader","limits"],["Trader","Technicals","levels"],["Trader","Fundamentals","news"],["Trader","Quant","signal_perf"],["Trader","Sentiment","shifts"],["Risk","PM","hedge_alert"],["Risk","Trader","hedge_alert"]],
"eod":[["Trader","PM","TCA"],["Risk","PM","stress_exposure"],["Fundamentals","PM","accuracy"],["Technicals","PM","accuracy"],["Quant","PM","attribution"],["Sentiment","PM","accuracy"],["PM","ALL","strategy_next_day"]]}
```