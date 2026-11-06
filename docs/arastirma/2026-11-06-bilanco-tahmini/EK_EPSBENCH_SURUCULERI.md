# EPSBench: 149 şirket-çeyrek şemasının tüm sürücüleri

Kaynak: [ticker_schemas_v4](https://github.com/chuyuxu/EPSBench/tree/main/stage_1_schema_building/ticker_schemas_v4). Kaynak veriler CC BY 4.0; atıf: EPSBench yazarları. Şemalar 2026-11-06 tarihinde incelendi.

Bunlar LLM tarafından tahmin edilen ara hedeflerdir. Sabit bir sayısal ML girdi listesi değildir. Şema adları, bire bir kalem ve çapa adları korundu. Şirkete özgü uzun açıklamalar kaynak dilinde tutuldu; işlem türünün Türkçe anlamı ayrıca verildi.

`yoy`: geçen yıl aynı döneme göre büyüme; `bps`: belirtilen çapa gelire oran değişimi (baz puan); `absolute`: doğrudan tutar/adet; `rate_override`: hedef oranın doğrudan belirlenmesi (baz puan değişimi değil). `shares` seyreltilmiş ağırlıklı ortalama hisse, `tax` vergi, `revenue/sales` gelir/satış, `cost/cogs` maliyet, `income` kâr/gelir, `expense` gider, `interest` faiz, `provision` karşılık, `noncontrolling` kontrol gücü olmayan paydır.

Tam özgün şemalar ve hesap formülleri [epsbench-semalar.json](epsbench-semalar.json) dosyasında. `_validation` hedef gerçekleri girdi sayılmamalı.

## ABBV_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_products_sold`, `selling_general_and_administrative`, `research_and_development`, `acquired_iprd_and_milestones`, `other_operating_income_net`, `interest_expense_net`, `net_foreign_exchange_loss`, `other_expense_net`, `net_earnings_attributable_to_noncontrolling_interest`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Net revenues YoY growth rate vs Q-4 |
| `cost_of_products_sold_margin_delta_bps` | `cost_of_products_sold / çapa: revenue` | Marj değişimi, baz puan | Cost of products sold as % of revenue, delta vs Q-4 |
| `selling_general_and_administrative_margin_delta_bps` | `selling_general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `acquired_iprd_and_milestones_yoy` | `acquired_iprd_and_milestones` | Yıllık büyüme | Acquired IPR&D and milestones expense YoY growth rate vs Q-4 |
| `other_operating_income_net_abs` | `other_operating_income_net` | Doğrudan tutar veya adet | other_operating_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `net_foreign_exchange_loss_abs` | `net_foreign_exchange_loss` | Doğrudan tutar veya adet | net_foreign_exchange_loss absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `net_earnings_attributable_to_noncontrolling_interest_abs` | `net_earnings_attributable_to_noncontrolling_interest` | Doğrudan tutar veya adet | net_earnings_attributable_to_noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## ADBE_2025Q4

Geçmiş dayanak kalemleri: `subscription_revenue`, `product_revenue`, `services_and_other_revenue`, `subscription_cogs`, `product_cogs`, `services_and_other_cogs`, `rd`, `sales_and_marketing`, `general_and_administrative`, `acquisition_termination_fee`, `amortization_of_intangibles`, `interest_expense`, `investment_gains_losses_net`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_revenue` | Yıllık büyüme | Subscription revenue YoY growth rate vs Q-4 |
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `services_and_other_revenue_yoy` | `services_and_other_revenue` | Yıllık büyüme | Services and other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `rd_margin_delta_bps` | `rd / çapa: total_revenue` | Marj değişimi, baz puan | R&D as % of total revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing as % of total revenue, delta vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | general_and_administrative YoY growth rate vs Q-4 |
| `acquisition_termination_fee_abs` | `acquisition_termination_fee` | Doğrudan tutar veya adet | acquisition_termination_fee absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `amortization_of_intangibles_yoy` | `amortization_of_intangibles` | Yıllık büyüme | amortization_of_intangibles YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_gains_losses_net_abs` | `investment_gains_losses_net` | Doğrudan tutar veya adet | investment_gains_losses_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## ADBE_2026Q1

Geçmiş dayanak kalemleri: `subscription_revenue`, `product_revenue`, `services_and_other_revenue`, `subscription_cogs`, `product_cogs`, `services_and_other_cogs`, `rd`, `sales_and_marketing`, `general_and_administrative`, `acquisition_termination_fee`, `amortization_of_intangibles`, `interest_expense`, `investment_gains`, `other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_revenue` | Yıllık büyüme | Subscription revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `total_opex_yoy` | `total_opex` | Yıllık büyüme | Total operating expense YoY growth rate vs Q-4 |
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | product_revenue YoY growth rate vs Q-4 |
| `services_and_other_revenue_yoy` | `services_and_other_revenue` | Yıllık büyüme | services_and_other_revenue YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_gains_abs` | `investment_gains` | Doğrudan tutar veya adet | investment_gains absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AMAT_2026Q1

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_products_sold`, `research_development_engineering`, `marketing_and_selling`, `general_and_administrative`, `interest_expense`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cost_of_products_sold_margin_delta_bps` | `cost_of_products_sold / çapa: net_revenue` | Marj değişimi, baz puan | Cost of products sold as % of net revenue, delta vs Q-4 |
| `research_development_engineering_yoy` | `research_development_engineering` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `total_sga_yoy` | `total_sga` | Yıllık büyüme | Combined selling and general admin expense YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AMAT_2026Q2

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_products_sold`, `rd`, `marketing_and_selling`, `general_and_administrative`, `interest_expense`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth vs Q-4 baseline |
| `cogs_margin_delta_bps` | `cost_of_products_sold / çapa: net_revenue` | Marj değişimi, baz puan | Cost of products sold as a percentage of net revenue, delta vs Q-4 baseline |
| `rd_yoy` | `rd` | Yıllık büyüme | Research, development and engineering expense YoY growth vs Q-4 baseline |
| `sga_margin_delta_bps` | `sga / çapa: net_revenue` | Marj değişimi, baz puan | SG&A (marketing and selling plus G&A) as a percentage of net revenue, delta vs Q-4 baseline |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## AMD_2025Q4

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_sales`, `amortization_acq_intangibles_cos`, `research_and_development`, `marketing_general_and_administrative`, `amortization_acq_intangibles_sga`, `restructuring_charges`, `licensing_gain`, `interest_expense`, `other_income_net`, `equity_income_in_investee`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cost_of_sales / çapa: net_revenue` | Marj değişimi, baz puan | Total cost of sales as % of net revenue, delta vs Q-4 |
| `rd_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `total_opex / çapa: net_revenue` | Marj değişimi, baz puan | SG&A expense as % of net revenue, delta vs Q-4 |
| `restructuring_charges_yoy` | `restructuring_charges` | Yıllık büyüme | Restructuring charges YoY growth rate vs Q-4 |
| `licensing_gain_yoy` | `licensing_gain` | Yıllık büyüme | Licensing gain YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_income_in_investee_abs` | `equity_income_in_investee` | Doğrudan tutar veya adet | equity_income_in_investee absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AMGN_2025Q4

Geçmiş dayanak kalemleri: `product_sales`, `other_revenues`, `cost_of_sales`, `research_and_development`, `selling_general_and_administrative`, `other_operating_expenses`, `interest_expense_net`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_sales_yoy` | `product_sales` | Yıllık büyüme | Product sales YoY growth rate vs Q-4 |
| `other_revenues_yoy` | `other_revenues` | Yıllık büyüme | Other revenues YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | COGS as % of total revenue, delta vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `selling_general_and_administrative_margin_delta_bps` | `selling_general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `other_operating_expenses_abs` | `other_operating_expenses` | Doğrudan tutar veya adet | other_operating_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_abs` | `interest_expense_net` | Doğrudan tutar veya adet | interest_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AMGN_2026Q1

Geçmiş dayanak kalemleri: `product_sales`, `other_revenues`, `cost_of_sales`, `rd`, `sga`, `other_opex`, `interest_expense_net`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_sales_yoy` | `product_sales` | Yıllık büyüme | Product sales YoY growth rate vs 2025Q1 |
| `other_revenues_yoy` | `other_revenues` | Yıllık büyüme | Other revenues YoY growth rate vs 2025Q1 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta bps vs 2025Q1 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs 2025Q1 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs 2025Q1 |
| `other_opex_yoy` | `other_opex` | Yıllık büyüme | Other operating expense YoY growth rate vs 2025Q1 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## AMZN_2025Q4

Geçmiş dayanak kalemleri: `products_revenue`, `services_revenue`, `cost_of_sales`, `fulfillment`, `technology_infrastructure`, `sales_and_marketing`, `general_and_administrative`, `other_operating_expense_net`, `interest_income`, `interest_expense`, `other_income_expense_net`, `equity_method_investment_activity_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Product sales YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Service sales YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `fulfillment_margin_delta_bps` | `fulfillment / çapa: total_revenue` | Marj değişimi, baz puan | Fulfillment expense as % of total revenue, delta vs Q-4 |
| `technology_infrastructure_margin_delta_bps` | `technology_infrastructure / çapa: total_revenue` | Marj değişimi, baz puan | Technology and infrastructure expense as % of total revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing expense as % of total revenue, delta vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | general_and_administrative YoY growth rate vs Q-4 |
| `other_operating_expense_net_abs` | `other_operating_expense_net` | Doğrudan tutar veya adet | other_operating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_method_investment_activity_net_abs` | `equity_method_investment_activity_net` | Doğrudan tutar veya adet | equity_method_investment_activity_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AVGO_2025Q4

Geçmiş dayanak kalemleri: `products_revenue`, `subscriptions_services_revenue`, `cost_of_products_sold`, `cost_of_subscriptions_services`, `amortization_acquisition_intangibles_cogs`, `restructuring_cogs`, `research_development`, `selling_general_administrative`, `amortization_acquisition_intangibles_opex`, `restructuring_opex`, `interest_expense`, `other_income_net`, `loss_from_discontinued_ops`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Hardware product revenue YoY growth rate vs Q-4 |
| `subscriptions_services_revenue_yoy` | `subscriptions_services_revenue` | Yıllık büyüme | Subscriptions and services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of revenue as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `research_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_yoy` | `selling_general_administrative` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `amortization_acquisition_intangibles_opex_yoy` | `amortization_acquisition_intangibles_opex` | Yıllık büyüme | amortization_acquisition_intangibles_opex YoY growth rate vs Q-4 |
| `restructuring_opex_abs` | `restructuring_opex` | Doğrudan tutar veya adet | restructuring_opex absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_from_discontinued_ops_abs` | `loss_from_discontinued_ops` | Doğrudan tutar veya adet | loss_from_discontinued_ops absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AVGO_2026Q1

Geçmiş dayanak kalemleri: `products_revenue`, `subscriptions_services_revenue`, `cost_of_products_sold`, `cost_of_subscriptions_services`, `amortization_acquisition_intangible_cogs`, `restructuring_charges_cogs`, `research_development`, `selling_general_administrative`, `amortization_acquisition_intangible_opex`, `restructuring_other_charges_opex`, `interest_expense`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Products revenue YoY growth rate vs Q-4 |
| `subscriptions_services_revenue_yoy` | `subscriptions_services_revenue` | Yıllık büyüme | Subscriptions and services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total cost of revenue as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `research_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `selling_general_administrative / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `amortization_acquisition_intangible_opex_yoy` | `amortization_acquisition_intangible_opex` | Yıllık büyüme | amortization_acquisition_intangible_opex YoY growth rate vs Q-4 |
| `restructuring_other_charges_opex_abs` | `restructuring_other_charges_opex` | Doğrudan tutar veya adet | restructuring_other_charges_opex absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AXP_2025Q4

Geçmiş dayanak kalemleri: `discount_revenue`, `net_card_fees`, `service_fees_other_revenue`, `processed_revenue`, `interest_on_loans`, `interest_and_dividends_on_investment_securities`, `deposits_with_banks_and_other`, `interest_expense_deposits`, `interest_expense_long_term_debt_and_other`, `provisions_card_member_receivables`, `provisions_card_member_loans`, `provisions_other`, `card_member_rewards`, `business_development`, `card_member_services`, `marketing`, `salaries_and_employee_benefits`, `other_expenses_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `discount_revenue_yoy` | `discount_revenue` | Yıllık büyüme | Discount revenue YoY growth rate vs Q-4 |
| `net_card_fees_yoy` | `net_card_fees` | Yıllık büyüme | Net card fees YoY growth rate vs Q-4 |
| `service_fees_other_revenue_yoy` | `service_fees_other_revenue` | Yıllık büyüme | Service fees and other revenue YoY growth rate vs Q-4 |
| `total_non_interest_revenues_margin_delta_bps` | `total_non_interest_revenues / çapa: total_revenue_net_of_interest_expense` | Marj değişimi, baz puan | Non-interest revenues as % of net revenue, delta vs Q-4 |
| `total_expenses_margin_delta_bps` | `total_expenses / çapa: total_revenue_net_of_interest_expense` | Marj değişimi, baz puan | Operating expenses as % of net revenue, delta vs Q-4 |
| `provisions_margin_delta_bps` | `total_provisions_for_credit_losses / çapa: total_revenue_net_of_interest_expense` | Marj değişimi, baz puan | Provision for credit losses as % of net revenue, delta vs Q-4 |
| `total_interest_income_yoy` | `total_interest_income` | Yıllık büyüme | Total interest income YoY growth rate vs Q-4 |
| `interest_expense_deposits_yoy` | `interest_expense_deposits` | Yıllık büyüme | interest_expense_deposits YoY growth rate vs Q-4 |
| `interest_expense_long_term_debt_and_other_yoy` | `interest_expense_long_term_debt_and_other` | Yıllık büyüme | interest_expense_long_term_debt_and_other YoY growth rate vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## AXP_2026Q1

Geçmiş dayanak kalemleri: `discount_revenue`, `net_card_fees`, `service_fees_and_other_revenue`, `interest_on_loans`, `interest_and_dividends_on_investment_securities`, `deposits_with_banks_and_other`, `deposits_interest_expense`, `long_term_debt_and_other_interest_expense`, `card_member_receivables_provision`, `card_member_loans_provision`, `other_provisions`, `card_member_rewards`, `business_development`, `card_member_services`, `marketing`, `salaries_and_employee_benefits`, `other_net`, `tax_rate`, `shares`, `participating_share_awards`, `preferred_dividends`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `discount_revenue_yoy` | `discount_revenue` | Yıllık büyüme | Card Member spend (discount revenue) YoY growth vs Q-4 |
| `net_card_fees_yoy` | `net_card_fees` | Yıllık büyüme | Net card fee revenue YoY growth vs Q-4 |
| `service_fees_and_other_revenue_yoy` | `service_fees_and_other_revenue` | Yıllık büyüme | Service fees and other revenue YoY growth vs Q-4 |
| `total_interest_income_yoy` | `total_interest_income` | Yıllık büyüme | Total interest income YoY growth vs Q-4 |
| `card_member_rewards_yoy` | `card_member_rewards` | Yıllık büyüme | Customer rewards expense YoY growth vs Q-4 |
| `provisions_margin_delta_bps` | `total_provisions_for_credit_losses / çapa: total_revenues_net_of_interest_expense` | Marj değişimi, baz puan | Total credit loss provisions as % of total revenues net of interest expense, delta vs Q-4 |
| `deposits_interest_expense_yoy` | `deposits_interest_expense` | Yıllık büyüme | deposits_interest_expense YoY growth rate vs Q-4 |
| `long_term_debt_and_other_interest_expense_yoy` | `long_term_debt_and_other_interest_expense` | Yıllık büyüme | long_term_debt_and_other_interest_expense YoY growth rate vs Q-4 |
| `business_development_yoy` | `business_development` | Yıllık büyüme | business_development YoY growth rate vs Q-4 |
| `card_member_services_yoy` | `card_member_services` | Yıllık büyüme | card_member_services YoY growth rate vs Q-4 |
| `marketing_yoy` | `marketing` | Yıllık büyüme | marketing YoY growth rate vs Q-4 |
| `salaries_and_employee_benefits_yoy` | `salaries_and_employee_benefits` | Yıllık büyüme | salaries_and_employee_benefits YoY growth rate vs Q-4 |
| `other_net_yoy` | `other_net` | Yıllık büyüme | other_net YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `participating_share_awards_abs` | `participating_share_awards` | Doğrudan tutar veya adet | participating_share_awards absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_dividends_abs` | `preferred_dividends` | Doğrudan tutar veya adet | preferred_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |

## BAC_2025Q4

Geçmiş dayanak kalemleri: `interest_income`, `interest_expense`, `fees_and_commissions`, `market_making_and_similar_activities`, `other_income_net`, `provision_for_credit_losses`, `compensation_and_benefits`, `occupancy_and_equipment`, `information_processing_and_communications`, `product_delivery_and_transaction_related`, `professional_fees`, `marketing`, `other_general_operating`, `preferred_stock_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `total_revenue_yoy` | `total_revenue` | Yıllık büyüme | Total net revenue YoY growth rate vs Q-4 |
| `noninterest_income_margin_delta_bps` | `total_noninterest_income / çapa: total_revenue` | Marj değişimi, baz puan | Noninterest income as % of total revenue, delta vs Q-4 |
| `provision_for_credit_losses_margin_delta_bps` | `provision_for_credit_losses / çapa: total_revenue` | Marj değişimi, baz puan | Provision for credit losses as % of total revenue, delta vs Q-4 |
| `noninterest_expense_margin_delta_bps` | `total_noninterest_expense / çapa: total_revenue` | Marj değişimi, baz puan | Total noninterest expense as % of total revenue, delta vs Q-4 |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## BA_2025Q4

Geçmiş dayanak kalemleri: `sales_of_products`, `sales_of_services`, `cost_of_products`, `cost_of_services`, `operating_investment_income`, `general_and_administrative`, `research_and_development`, `gain_on_dispositions`, `other_income`, `interest_expense`, `nci_loss`, `preferred_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `sales_of_products` | Yıllık büyüme | Products revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `sales_of_services` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | SG&A (G&A) as % of total revenue, delta vs Q-4 |
| `operating_investment_income_abs` | `operating_investment_income` | Doğrudan tutar veya adet | operating_investment_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `gain_on_dispositions_abs` | `gain_on_dispositions` | Doğrudan tutar veya adet | gain_on_dispositions absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `nci_loss_abs` | `nci_loss` | Doğrudan tutar veya adet | nci_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_dividends_abs` | `preferred_dividends` | Doğrudan tutar veya adet | preferred_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## BBY_2026Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `sga`, `restructuring_charges`, `goodwill_impairment`, `investment_income_other`, `interest_expense`, `gain_on_sale_subsidiary`, `equity_income_affiliates`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as % of revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `restructuring_charges_abs` | `restructuring_charges` | Doğrudan tutar veya adet | restructuring_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `goodwill_impairment_abs` | `goodwill_impairment` | Doğrudan tutar veya adet | goodwill_impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `investment_income_other_abs` | `investment_income_other` | Doğrudan tutar veya adet | investment_income_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `gain_on_sale_subsidiary_abs` | `gain_on_sale_subsidiary` | Doğrudan tutar veya adet | gain_on_sale_subsidiary absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_income_affiliates_abs` | `equity_income_affiliates` | Doğrudan tutar veya adet | equity_income_affiliates absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## BBY_2027Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `sga`, `restructuring_charges`, `investment_income_and_other`, `interest_expense`, `equity_in_income_loss_of_affiliates`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs 2026Q1 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as % of revenue, delta bps vs 2026Q1 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A expense as % of revenue, delta bps vs 2026Q1 |
| `restructuring_yoy` | `restructuring_charges` | Yıllık büyüme | Restructuring charges YoY growth rate vs 2026Q1 |
| `investment_income_and_other_abs` | `investment_income_and_other` | Doğrudan tutar veya adet | investment_income_and_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `equity_in_income_loss_of_affiliates_abs` | `equity_in_income_loss_of_affiliates` | Doğrudan tutar veya adet | equity_in_income_loss_of_affiliates absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## BLK_2025Q4

Geçmiş dayanak kalemleri: `adv_and_sec_lending_revenue`, `performance_fees`, `technology_services_revenue`, `distribution_fees`, `advisory_other_revenue`, `employee_compensation`, `distribution_servicing_costs`, `direct_fund_expense`, `sub_advisory_other`, `general_administration`, `other_operating_expenses`, `non_operating_income`, `nci`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `total_revenue_yoy` | `total_revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `employee_compensation_margin_delta_bps` | `employee_compensation / çapa: total_revenue` | Marj değişimi, baz puan | Employee compensation as % of total revenue, delta vs Q-4 |
| `sales_asset_margin_delta_bps` | `total_sales_asset / çapa: total_revenue` | Marj değişimi, baz puan | Sales, asset and account expense as % of total revenue, delta vs Q-4 |
| `general_administration_margin_delta_bps` | `general_administration / çapa: total_revenue` | Marj değişimi, baz puan | General and administration expense as % of total revenue, delta vs Q-4 |
| `other_operating_expenses_yoy` | `other_operating_expenses` | Yıllık büyüme | Other operating expenses (amortization, restructuring, contingent consideration) YoY growth rate vs Q-4 |
| `non_operating_income_yoy` | `non_operating_income` | Yıllık büyüme | Non-operating income YoY growth rate vs Q-4 |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## BLK_2026Q1

Geçmiş dayanak kalemleri: `related_party_advisory_fees`, `third_party_advisory_fees`, `performance_fees`, `technology_services_revenue`, `distribution_fees`, `advisory_other_revenue`, `compensation_benefits`, `distribution_servicing_costs`, `direct_fund_expense`, `sub_advisory_other_expense`, `general_administration_expense`, `amortization_intangibles`, `net_gain_investments`, `interest_dividend_income`, `interest_expense`, `income_taxes`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `advisory_fees_yoy` | `investment_advisory_fees_total` | Yıllık büyüme | Total investment advisory, administration fees and securities lending revenue YoY growth |
| `performance_fees_yoy` | `performance_fees` | Yıllık büyüme | Investment advisory performance fees YoY growth |
| `technology_services_revenue_yoy` | `technology_services_revenue` | Yıllık büyüme | Technology services and subscription revenue YoY growth |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Distribution fees plus advisory and other revenue YoY growth |
| `compensation_margin_delta_bps` | `compensation_benefits / çapa: total_revenue` | Marj değişimi, baz puan | Employee compensation and benefits as a percentage of total revenue, change vs Q-4 in bps |
| `other_operating_expense_margin_delta_bps` | `total_other_operating_expense / çapa: total_revenue` | Marj değişimi, baz puan | All non-compensation operating expenses as a percentage of total revenue, change vs Q-4 in bps |
| `net_gain_investments_abs` | `net_gain_investments` | Doğrudan tutar veya adet | net_gain_investments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_dividend_income_yoy` | `interest_dividend_income` | Yıllık büyüme | interest_dividend_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CAT_2025Q4

Geçmiş dayanak kalemleri: `machinery_revenue`, `financial_products_revenue`, `cogs`, `sga`, `rd`, `interest_expense_financial_products`, `goodwill_impairment_charge`, `other_operating_expenses`, `interest_expense`, `other_income_net`, `pretax_income`, `tax_rate`, `equity_income`, `profit_attrib_to_noncontrolling_interests`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `machinery_revenue_yoy` | `machinery_revenue` | Yıllık büyüme | Machinery, Energy & Transportation revenue YoY growth rate vs Q-4 |
| `financial_products_revenue_yoy` | `financial_products_revenue` | Yıllık büyüme | Financial Products revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cogs / çapa: total_revenue` | Marj değişimi, baz puan | COGS as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `rd_margin_delta_bps` | `rd / çapa: total_revenue` | Marj değişimi, baz puan | R&D expense as % of total revenue, delta vs Q-4 |
| `interest_expense_financial_products_margin_delta_bps` | `interest_expense_financial_products / çapa: total_revenue` | Marj değişimi, baz puan | Interest expense of Financial Products as % of total revenue, delta vs Q-4 |
| `goodwill_impairment_charge_abs` | `goodwill_impairment_charge` | Doğrudan tutar veya adet | goodwill_impairment_charge absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_operating_expenses_abs` | `other_operating_expenses` | Doğrudan tutar veya adet | other_operating_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_income_abs` | `equity_income` | Doğrudan tutar veya adet | equity_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `profit_attrib_to_noncontrolling_interests_abs` | `profit_attrib_to_noncontrolling_interests` | Doğrudan tutar veya adet | profit_attrib_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CAT_2026Q1

Geçmiş dayanak kalemleri: `sales_of_machinery_energy_transportation`, `revenues_of_financial_products`, `cost_of_goods_sold`, `selling_general_and_administrative_expenses`, `research_and_development_expenses`, `interest_expense_of_financial_products`, `other_operating_income_expenses`, `interest_expense_excluding_financial_products`, `other_income_expense`, `equity_in_profit_of_unconsolidated_affiliates`, `noncontrolling_interest`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `met_sales_yoy` | `sales_of_machinery_energy_transportation` | Yıllık büyüme | Machinery, Energy & Transportation sales YoY growth vs Q-4 |
| `financial_products_revenues_yoy` | `revenues_of_financial_products` | Yıllık büyüme | Financial Products revenues YoY growth vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_goods_sold / çapa: total_revenue` | Marj değişimi, baz puan | COGS as % of total sales and revenues, delta vs Q-4 |
| `sga_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total sales and revenues, delta vs Q-4 |
| `rd_margin_delta_bps` | `research_and_development_expenses / çapa: total_revenue` | Marj değişimi, baz puan | R&D as % of total sales and revenues, delta vs Q-4 |
| `other_operating_expenses_margin_delta_bps` | `other_operating_income_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Other operating expenses as % of total sales and revenues, delta vs Q-4 |
| `interest_expense_of_financial_products_yoy` | `interest_expense_of_financial_products` | Yıllık büyüme | interest_expense_of_financial_products YoY growth rate vs Q-4 |
| `interest_expense_excluding_financial_products_yoy` | `interest_expense_excluding_financial_products` | Yıllık büyüme | interest_expense_excluding_financial_products YoY growth rate vs Q-4 |
| `other_income_expense_abs` | `other_income_expense` | Doğrudan tutar veya adet | other_income_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_profit_of_unconsolidated_affiliates_abs` | `equity_in_profit_of_unconsolidated_affiliates` | Doğrudan tutar veya adet | equity_in_profit_of_unconsolidated_affiliates absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CCL_2025Q4

Geçmiş dayanak kalemleri: `passenger_ticket`, `onboard_and_other`, `commissions_transportation_and_other`, `onboard_and_other_operating`, `payroll_and_related`, `fuel`, `food`, `ship_and_other_impairments`, `other_operating`, `selling_and_administrative`, `depreciation_and_amortization`, `interest_income`, `interest_expense_net_of_capitalized_interest`, `debt_extinguishment_and_modification_costs`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_ticket_yoy` | `passenger_ticket` | Yıllık büyüme | Passenger ticket revenue YoY growth rate vs Q-4 |
| `onboard_and_other_yoy` | `onboard_and_other` | Yıllık büyüme | Onboard and other revenue YoY growth rate vs Q-4 |
| `fuel_yoy` | `fuel` | Yıllık büyüme | Fuel expense YoY growth rate vs Q-4 |
| `cruise_and_tour_operating_expenses_margin_delta_bps` | `total_cruise_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Cruise and tour operating expenses as % of total revenue, delta vs Q-4 |
| `selling_and_administrative_margin_delta_bps` | `selling_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | Selling and administrative expense as % of total revenue, delta vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_net_of_capitalized_interest_yoy` | `interest_expense_net_of_capitalized_interest` | Yıllık büyüme | interest_expense_net_of_capitalized_interest YoY growth rate vs Q-4 |
| `debt_extinguishment_and_modification_costs_abs` | `debt_extinguishment_and_modification_costs` | Doğrudan tutar veya adet | debt_extinguishment_and_modification_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CCL_2026Q1

Geçmiş dayanak kalemleri: `passenger_ticket`, `onboard_other`, `commissions_transportation_other`, `onboard_other_expense`, `payroll_related`, `fuel`, `food`, `other_operating`, `selling_administrative`, `depreciation_amortization`, `interest_income`, `interest_expense`, `debt_extinguishment_costs`, `other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_ticket_yoy` | `passenger_ticket` | Yıllık büyüme | Passenger ticket revenue YoY growth rate vs Q-4 |
| `onboard_other_yoy` | `onboard_other` | Yıllık büyüme | Onboard and other revenue YoY growth rate vs Q-4 |
| `fuel_margin_delta_bps` | `fuel / çapa: total_revenue` | Marj değişimi, baz puan | Fuel expense as % of total revenue, delta vs Q-4 |
| `selling_administrative_margin_delta_bps` | `selling_administrative / çapa: total_revenue` | Marj değişimi, baz puan | Selling and administrative as % of total revenue, delta vs Q-4 |
| `commissions_transportation_other_yoy` | `commissions_transportation_other` | Yıllık büyüme | commissions_transportation_other YoY growth rate vs Q-4 |
| `onboard_other_expense_abs` | `onboard_other_expense` | Doğrudan tutar veya adet | onboard_other_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `payroll_related_yoy` | `payroll_related` | Yıllık büyüme | payroll_related YoY growth rate vs Q-4 |
| `food_yoy` | `food` | Yıllık büyüme | food YoY growth rate vs Q-4 |
| `other_operating_abs` | `other_operating` | Doğrudan tutar veya adet | other_operating absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `depreciation_amortization_yoy` | `depreciation_amortization` | Yıllık büyüme | depreciation_amortization YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `debt_extinguishment_costs_abs` | `debt_extinguishment_costs` | Doğrudan tutar veya adet | debt_extinguishment_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CCL_2026Q2

Geçmiş dayanak kalemleri: `passenger_ticket_revenue`, `onboard_and_other_revenue`, `commissions_transportation_and_other`, `onboard_and_other_expense`, `payroll_and_related`, `fuel`, `food`, `other_operating`, `selling_and_administrative`, `depreciation_and_amortization`, `interest_income`, `interest_expense`, `debt_extinguishment_and_modification_costs`, `other_income_expense_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_ticket_revenue_yoy` | `passenger_ticket_revenue` | Yıllık büyüme | Passenger ticket revenue YoY growth rate vs Q-4 (2025Q2) |
| `onboard_and_other_revenue_yoy` | `onboard_and_other_revenue` | Yıllık büyüme | Onboard and other revenue YoY growth rate vs Q-4 (2025Q2) |
| `cruise_cost_margin_delta_bps` | `total_cruise_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Total cruise and tour operating expenses as % of total revenue, delta vs Q-4 |
| `selling_and_administrative_margin_delta_bps` | `selling_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | Selling and administrative expenses as % of total revenue, delta vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | Depreciation and amortization YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `debt_extinguishment_and_modification_costs_abs` | `debt_extinguishment_and_modification_costs` | Doğrudan tutar veya adet | debt_extinguishment_and_modification_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CMCSA_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `programming_and_production`, `marketing_and_promotion`, `other_operating_and_administrative`, `depreciation`, `amortization`, `goodwill_and_longlived_asset_impairments`, `interest_expense`, `investment_and_other_income_net`, `tax_rate`, `shares`, `net_income`, `net_income_attributable_to_noncontrolling_interests`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `programming_and_production_margin_delta_bps` | `programming_and_production / çapa: revenue` | Marj değişimi, baz puan | Programming and production as % of revenue, delta vs Q-4 |
| `marketing_and_promotion_margin_delta_bps` | `marketing_and_promotion / çapa: revenue` | Marj değişimi, baz puan | Marketing and promotion as % of revenue, delta vs Q-4 |
| `other_operating_and_administrative_margin_delta_bps` | `other_operating_and_administrative / çapa: revenue` | Marj değişimi, baz puan | Other operating and administrative as % of revenue, delta vs Q-4 |
| `depreciation_margin_delta_bps` | `depreciation / çapa: revenue` | Marj değişimi, baz puan | Depreciation as % of revenue, delta vs Q-4 |
| `amortization_margin_delta_bps` | `amortization / çapa: revenue` | Marj değişimi, baz puan | Amortization as % of revenue, delta vs Q-4 |
| `goodwill_and_longlived_asset_impairments_abs` | `goodwill_and_longlived_asset_impairments` | Doğrudan tutar veya adet | goodwill_and_longlived_asset_impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_and_other_income_net_abs` | `investment_and_other_income_net` | Doğrudan tutar veya adet | investment_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `net_income_abs` | `net_income` | Doğrudan tutar veya adet | net_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |

## CMCSA_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `programming_and_production`, `marketing_and_promotion`, `other_operating_and_administrative`, `depreciation`, `amortization`, `interest_expense`, `investment_other_loss_net`, `tax_rate`, `noncontrolling_interest`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 baseline |
| `programming_and_production_margin_delta_bps` | `programming_and_production / çapa: revenue` | Marj değişimi, baz puan | Programming and production costs as % of revenue, delta vs Q-4 |
| `marketing_and_promotion_margin_delta_bps` | `marketing_and_promotion / çapa: revenue` | Marj değişimi, baz puan | Marketing and promotion expense as % of revenue, delta vs Q-4 |
| `other_operating_and_administrative_margin_delta_bps` | `other_operating_and_administrative / çapa: revenue` | Marj değişimi, baz puan | Other operating and administrative expense as % of revenue, delta vs Q-4 |
| `d_and_a_margin_delta_bps` | `d_and_a / çapa: revenue` | Marj değişimi, baz puan | Depreciation and amortization as % of revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_other_loss_net_abs` | `investment_other_loss_net` | Doğrudan tutar veya adet | investment_other_loss_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CMG_2025Q4

Geçmiş dayanak kalemleri: `food_and_beverage_revenue`, `delivery_service_revenue`, `food_beverage_and_packaging`, `labor`, `occupancy`, `other_operating_costs`, `general_and_administrative_expenses`, `depreciation_and_amortization`, `pre_opening_costs`, `impairment_closure_costs_and_asset_disposals`, `interest_and_other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `food_and_beverage_revenue_yoy` | `food_and_beverage_revenue` | Yıllık büyüme | Food and beverage revenue YoY growth rate vs Q-4 |
| `delivery_service_revenue_yoy` | `delivery_service_revenue` | Yıllık büyüme | Delivery service revenue YoY growth rate vs Q-4 |
| `food_beverage_and_packaging_margin_delta_bps` | `food_beverage_and_packaging / çapa: total_revenue` | Marj değişimi, baz puan | Food and beverage packaging cost as % of total revenue, delta vs Q-4 |
| `labor_margin_delta_bps` | `labor / çapa: total_revenue` | Marj değişimi, baz puan | Labor expense as % of total revenue, delta vs Q-4 |
| `occupancy_margin_delta_bps` | `occupancy / çapa: total_revenue` | Marj değişimi, baz puan | Occupancy expense as % of total revenue, delta vs Q-4 |
| `general_and_administrative_expenses_margin_delta_bps` | `general_and_administrative_expenses / çapa: total_revenue` | Marj değişimi, baz puan | G&A expense as % of total revenue, delta vs Q-4 |
| `other_operating_costs_abs` | `other_operating_costs` | Doğrudan tutar veya adet | other_operating_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `pre_opening_costs_yoy` | `pre_opening_costs` | Yıllık büyüme | pre_opening_costs YoY growth rate vs Q-4 |
| `impairment_closure_costs_and_asset_disposals_abs` | `impairment_closure_costs_and_asset_disposals` | Doğrudan tutar veya adet | impairment_closure_costs_and_asset_disposals absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CMG_2026Q1

Geçmiş dayanak kalemleri: `food_and_beverage_revenue`, `delivery_service_revenue`, `food_beverage_and_packaging`, `labor`, `occupancy`, `other_operating_costs`, `general_and_administrative_expenses`, `depreciation_and_amortization`, `pre_opening_costs`, `impairment_closure_costs_and_asset_disposals`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `food_and_beverage_revenue_yoy` | `food_and_beverage_revenue` | Yıllık büyüme | YoY growth rate for food and beverage revenue vs 2025Q1 |
| `delivery_service_revenue_yoy` | `delivery_service_revenue` | Yıllık büyüme | YoY growth rate for delivery service revenue vs 2025Q1 |
| `restaurant_operating_costs_margin_delta_bps` | `restaurant_operating_costs / çapa: total_revenue` | Marj değişimi, baz puan | Combined restaurant operating costs as % of total revenue, delta vs 2025Q1 |
| `general_and_administrative_expenses_yoy` | `general_and_administrative_expenses` | Yıllık büyüme | YoY growth rate for G&A expense vs 2025Q1 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | YoY growth rate for depreciation and amortization vs 2025Q1 |
| `development_and_closure_costs_yoy` | `development_and_closure_costs` | Yıllık büyüme | YoY growth rate for combined pre-opening and impairment/closure costs vs 2025Q1 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COIN_2025Q4

Geçmiş dayanak kalemleri: `net_revenue`, `other_revenue`, `transaction_expense`, `tech_development`, `sales_marketing`, `general_administrative`, `gains_on_crypto_operations_net`, `crypto_impairment_net`, `restructuring`, `other_operating_expense_net`, `interest_expense`, `gains_on_crypto_investment_net`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `transaction_expense_margin_delta_bps` | `transaction_expense / çapa: total_revenue` | Marj değişimi, baz puan | Transaction expense as % of total revenue, delta vs Q-4 |
| `tech_development_margin_delta_bps` | `tech_development / çapa: total_revenue` | Marj değişimi, baz puan | Tech and development expense as % of total revenue, delta vs Q-4 |
| `sales_marketing_margin_delta_bps` | `sales_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing expense as % of total revenue, delta vs Q-4 |
| `general_administrative_margin_delta_bps` | `general_administrative / çapa: total_revenue` | Marj değişimi, baz puan | General and administrative expense as % of total revenue, delta vs Q-4 |
| `gains_on_crypto_operations_net_abs` | `gains_on_crypto_operations_net` | Doğrudan tutar veya adet | gains_on_crypto_operations_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `crypto_impairment_net_abs` | `crypto_impairment_net` | Doğrudan tutar veya adet | crypto_impairment_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_operating_expense_net_abs` | `other_operating_expense_net` | Doğrudan tutar veya adet | other_operating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `gains_on_crypto_investment_net_abs` | `gains_on_crypto_investment_net` | Doğrudan tutar veya adet | gains_on_crypto_investment_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COIN_2026Q1

Geçmiş dayanak kalemleri: `net_revenue`, `other_revenue`, `transaction_expense`, `technology_and_development`, `sales_and_marketing`, `general_and_administrative`, `crypto_operating_losses`, `other_operating_income_net`, `interest_expense`, `crypto_investment_losses`, `other_expense_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Transaction revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Subscription, stablecoin, and other non-transaction revenue YoY growth rate vs Q-4 |
| `core_opex_margin_delta_bps` | `core_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Core operating expenses as % of total revenue, delta vs Q-4 |
| `crypto_operating_losses_yoy` | `crypto_operating_losses` | Yıllık büyüme | Net losses on crypto assets held for operations YoY growth rate vs Q-4 |
| `crypto_investment_losses_yoy` | `crypto_investment_losses` | Yıllık büyüme | Net losses on crypto assets held for investment YoY growth rate vs Q-4 |
| `other_operating_income_net_abs` | `other_operating_income_net` | Doğrudan tutar veya adet | other_operating_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COP_2025Q4

Geçmiş dayanak kalemleri: `sales_revenue`, `other_operating_income`, `purchased_commodities`, `production_and_operating_expenses`, `sga`, `exploration`, `depreciation`, `impairments`, `taxes_other_than_income`, `accretion`, `interest_debt`, `other_operating_expenses_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_revenue_yoy` | `sales_revenue` | Yıllık büyüme | Sales and other operating revenues YoY growth rate vs Q-4 |
| `other_operating_income_yoy` | `other_operating_income` | Yıllık büyüme | Other operating income (equity earnings, gain/loss on dispositions, other) YoY growth rate vs Q-4 |
| `purchased_commodities_margin_delta_bps` | `purchased_commodities / çapa: total_revenue` | Marj değişimi, baz puan | Purchased commodities as % of total revenue, delta vs Q-4 |
| `production_costs_margin_delta_bps` | `production_and_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Production and operating expenses as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | Selling, general and administrative expenses as % of total revenue, delta vs Q-4 |
| `depreciation_margin_delta_bps` | `depreciation / çapa: total_revenue` | Marj değişimi, baz puan | Depreciation, depletion and amortization as % of total revenue, delta vs Q-4 |
| `exploration_yoy` | `exploration` | Yıllık büyüme | exploration YoY growth rate vs Q-4 |
| `impairments_abs` | `impairments` | Doğrudan tutar veya adet | impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `taxes_other_than_income_yoy` | `taxes_other_than_income` | Yıllık büyüme | taxes_other_than_income YoY growth rate vs Q-4 |
| `accretion_abs` | `accretion` | Doğrudan tutar veya adet | accretion absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_debt_yoy` | `interest_debt` | Yıllık büyüme | interest_debt YoY growth rate vs Q-4 |
| `other_operating_expenses_net_abs` | `other_operating_expenses_net` | Doğrudan tutar veya adet | other_operating_expenses_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COP_2026Q1

Geçmiş dayanak kalemleri: `sales_and_other_operating_revenues`, `equity_in_earnings_of_affiliates`, `gain_on_dispositions`, `other_income`, `purchased_commodities`, `production_and_operating_expenses`, `sga`, `exploration_expenses`, `depreciation_depletion_amortization`, `impairments`, `taxes_other_than_income_taxes`, `accretion_on_discounted_liabilities`, `interest_and_debt_expense`, `foreign_currency_transaction_loss`, `other_expenses`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `total_revenues_yoy` | `total_revenues_and_other_income` | Yıllık büyüme | Total revenues and other income YoY growth rate vs Q-4 |
| `purchased_commodities_margin_delta_bps` | `purchased_commodities / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Purchased commodities as % of total revenues, basis point change vs Q-4 |
| `production_and_operating_expenses_margin_delta_bps` | `production_and_operating_expenses / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Production and operating expenses as % of total revenues, basis point change vs Q-4 |
| `depreciation_depletion_amortization_yoy` | `depreciation_depletion_amortization` | Yıllık büyüme | DD&A expense YoY growth rate vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `exploration_expenses_yoy` | `exploration_expenses` | Yıllık büyüme | exploration_expenses YoY growth rate vs Q-4 |
| `impairments_abs` | `impairments` | Doğrudan tutar veya adet | impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `taxes_other_than_income_taxes_yoy` | `taxes_other_than_income_taxes` | Yıllık büyüme | taxes_other_than_income_taxes YoY growth rate vs Q-4 |
| `accretion_on_discounted_liabilities_abs` | `accretion_on_discounted_liabilities` | Doğrudan tutar veya adet | accretion_on_discounted_liabilities absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_debt_expense_yoy` | `interest_and_debt_expense` | Yıllık büyüme | interest_and_debt_expense YoY growth rate vs Q-4 |
| `foreign_currency_transaction_loss_abs` | `foreign_currency_transaction_loss` | Doğrudan tutar veya adet | foreign_currency_transaction_loss absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_expenses_abs` | `other_expenses` | Doğrudan tutar veya adet | other_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COST_2026Q1

Geçmiş dayanak kalemleri: `net_sales`, `membership_fees`, `merchandise_costs`, `sga`, `interest_expense`, `interest_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `membership_fees_yoy` | `membership_fees` | Yıllık büyüme | Membership fees YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Merchandise costs as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_net_yoy` | `interest_income_net` | Yıllık büyüme | interest_income_net YoY growth rate vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## COST_2026Q2

Geçmiş dayanak kalemleri: `net_sales`, `membership_fees`, `merchandise_costs`, `sga`, `interest_expense`, `interest_income_other`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `membership_fees_yoy` | `membership_fees` | Yıllık büyüme | Membership fees YoY growth rate vs Q-4 |
| `merchandise_costs_margin_delta_bps` | `merchandise_costs / çapa: total_revenue` | Marj değişimi, baz puan | Merchandise costs as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_other_yoy` | `interest_income_other` | Yıllık büyüme | interest_income_other YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## COST_2026Q3

Geçmiş dayanak kalemleri: `net_sales`, `membership_fees`, `merchandise_costs`, `sga`, `interest_expense`, `interest_income_and_other_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `membership_fees_yoy` | `membership_fees` | Yıllık büyüme | Membership fee revenue YoY growth rate vs Q-4 |
| `merchandise_costs_margin_delta_bps` | `merchandise_costs / çapa: total_revenue` | Marj değişimi, baz puan | Merchandise costs as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `interest_income_and_other_net_yoy` | `interest_income_and_other_net` | Yıllık büyüme | Interest income and other, net YoY growth vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CRM_2027Q1

Geçmiş dayanak kalemleri: `subscription_and_support_revenue`, `services_revenue`, `subscription_and_support_cost_of_revenue`, `services_cost_of_revenue`, `rd`, `sales_and_marketing`, `general_and_administrative`, `restructuring`, `strategic_investment_losses`, `other_income`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_and_support_revenue` | Yıllık büyüme | Subscription and support revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Professional services and other revenue YoY growth rate vs Q-4 |
| `cost_of_revenue_margin_delta_bps` | `total_cost_of_revenue / çapa: total_revenue` | Marj değişimi, baz puan | Total cost of revenues as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing as % of total revenue, delta vs Q-4 |
| `g_and_a_margin_delta_bps` | `general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | General and administrative as % of total revenue, delta vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `strategic_investment_losses_abs` | `strategic_investment_losses` | Doğrudan tutar veya adet | strategic_investment_losses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CRWD_2026Q3

Geçmiş dayanak kalemleri: `subscription_revenue`, `professional_services_revenue`, `subscription_cost`, `professional_services_cost`, `sales_and_marketing`, `research_and_development`, `general_and_administrative`, `interest_expense`, `interest_income`, `other_income_expense_net`, `noncontrolling_interest`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_revenue` | Yıllık büyüme | Subscription revenue YoY growth rate vs Q-4 |
| `professional_services_revenue_yoy` | `professional_services_revenue` | Yıllık büyüme | Professional services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sales_and_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | G&A expense YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CRWD_2026Q4

Geçmiş dayanak kalemleri: `subscription_revenue`, `professional_services_revenue`, `subscription_cogs`, `professional_services_cogs`, `sales_and_marketing`, `research_and_development`, `general_and_administrative`, `interest_expense`, `interest_income`, `other_income_net`, `pretax_income`, `noncontrolling_interest`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_revenue` | Yıllık büyüme | Subscription revenue YoY growth rate vs Q-4 |
| `professional_services_revenue_yoy` | `professional_services_revenue` | Yıllık büyüme | Professional services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing expense as % of total revenue, delta vs Q-4 |
| `research_and_development_margin_delta_bps` | `research_and_development / çapa: total_revenue` | Marj değişimi, baz puan | R&D expense as % of total revenue, delta vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | G&A expense as % of total revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `pretax_income_abs` | `pretax_income` | Doğrudan tutar veya adet | pretax_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CRWD_2027Q1

Geçmiş dayanak kalemleri: `subscription_revenue`, `professional_services_revenue`, `subscription_cost_of_revenue`, `professional_services_cost_of_revenue`, `sales_marketing_expense`, `research_development_expense`, `general_administrative_expense`, `interest_expense`, `interest_income`, `other_income_net`, `income_taxes`, `noncontrolling_interest`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `subscription_revenue_yoy` | `subscription_revenue` | Yıllık büyüme | Subscription revenue YoY growth rate vs Q4 baseline |
| `professional_services_revenue_yoy` | `professional_services_revenue` | Yıllık büyüme | Professional services revenue YoY growth rate vs Q4 baseline |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of revenue as % of total revenue, delta vs Q4 baseline |
| `sales_marketing_yoy` | `sales_marketing_expense` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q4 baseline |
| `rd_yoy` | `research_development_expense` | Yıllık büyüme | Research and development expense YoY growth rate vs Q4 baseline |
| `ga_yoy` | `general_administrative_expense` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q4 baseline |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CSCO_2026Q2

Geçmiş dayanak kalemleri: `product_revenue`, `services_revenue`, `product_cogs`, `services_cogs`, `rd`, `sales_marketing`, `general_administrative`, `amortization_intangibles`, `restructuring_charges`, `interest_income`, `interest_expense`, `other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_marketing_margin_delta_bps` | `sales_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing as % of total revenue, delta vs Q-4 |
| `general_administrative_yoy` | `general_administrative` | Yıllık büyüme | general_administrative YoY growth rate vs Q-4 |
| `amortization_intangibles_yoy` | `amortization_intangibles` | Yıllık büyüme | amortization_intangibles YoY growth rate vs Q-4 |
| `restructuring_charges_abs` | `restructuring_charges` | Doğrudan tutar veya adet | restructuring_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CSCO_2026Q3

Geçmiş dayanak kalemleri: `product_revenue`, `services_revenue`, `product_cogs`, `services_cogs`, `rd`, `sales_and_marketing`, `general_and_administrative`, `amortization_of_purchased_intangibles`, `restructuring_and_other_charges`, `interest_income`, `interest_expense`, `other_income_loss_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs 2025Q3 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs 2025Q3 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total cost of sales as % of total revenue, delta vs 2025Q3 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs 2025Q3 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing expense as % of total revenue, delta vs 2025Q3 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | General and administrative expense as % of total revenue, delta vs 2025Q3 |
| `amortization_of_purchased_intangibles_yoy` | `amortization_of_purchased_intangibles` | Yıllık büyüme | amortization_of_purchased_intangibles YoY growth rate vs Q-4 |
| `restructuring_and_other_charges_abs` | `restructuring_and_other_charges` | Doğrudan tutar veya adet | restructuring_and_other_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_loss_net_abs` | `other_income_loss_net` | Doğrudan tutar veya adet | other_income_loss_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CVNA_2025Q4

Geçmiş dayanak kalemleri: `retail_vehicle_sales_net`, `wholesale_sales_revenues`, `other_sales_revenues`, `net_sales_operating_revenues`, `cost_of_sales`, `selling_general_and_administrative_expenses`, `goodwill_impairment`, `other_operating_expense_net`, `interest_expense`, `loss_gain_on_debt_extinguishment`, `other_income_expense_net`, `pretax_income`, `noncontrolling_interest`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_operating_revenues_yoy` | `net_sales_operating_revenues` | Yıllık büyüme | Net sales and operating revenues YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: net_sales_operating_revenues` | Marj değişimi, baz puan | Cost of sales as % of net sales and operating revenues, delta vs Q-4 |
| `selling_general_and_administrative_expenses_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: net_sales_operating_revenues` | Marj değişimi, baz puan | SG&A expenses as % of net sales and operating revenues, delta vs Q-4 |
| `retail_vehicle_sales_net_abs` | `retail_vehicle_sales_net` | Doğrudan tutar veya adet | retail_vehicle_sales_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `wholesale_sales_revenues_abs` | `wholesale_sales_revenues` | Doğrudan tutar veya adet | wholesale_sales_revenues absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `other_sales_revenues_abs` | `other_sales_revenues` | Doğrudan tutar veya adet | other_sales_revenues absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `goodwill_impairment_abs` | `goodwill_impairment` | Doğrudan tutar veya adet | goodwill_impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_operating_expense_net_abs` | `other_operating_expense_net` | Doğrudan tutar veya adet | other_operating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `loss_gain_on_debt_extinguishment_abs` | `loss_gain_on_debt_extinguishment` | Doğrudan tutar veya adet | loss_gain_on_debt_extinguishment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CVNA_2026Q1

Geçmiş dayanak kalemleri: `retail_vehicle_sales`, `wholesale_sales_and_revenues`, `other_sales_and_revenues`, `cost_of_sales`, `sga`, `other_operating_expense_net`, `interest_expense_net`, `loss_on_debt_extinguishment`, `other_income_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `retail_vehicle_sales_yoy` | `retail_vehicle_sales` | Yıllık büyüme | Retail vehicle sales YoY growth rate vs Q-4 |
| `wholesale_sales_and_revenues_yoy` | `wholesale_sales_and_revenues` | Yıllık büyüme | Wholesale sales and revenues YoY growth rate vs Q-4 |
| `other_sales_and_revenues_yoy` | `other_sales_and_revenues` | Yıllık büyüme | Other sales and revenues YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `interest_expense_margin_delta_bps` | `interest_expense_net / çapa: total_revenue` | Marj değişimi, baz puan | Net interest expense as % of total revenue, delta vs Q-4 |
| `other_operating_expense_net_abs` | `other_operating_expense_net` | Doğrudan tutar veya adet | other_operating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_on_debt_extinguishment_abs` | `loss_on_debt_extinguishment` | Doğrudan tutar veya adet | loss_on_debt_extinguishment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## CVX_2025Q4

Geçmiş dayanak kalemleri: `sales_and_other_operating_revenues`, `income_from_equity_affiliates`, `other_income_net`, `purchased_crude_oil_and_products`, `operating_expenses`, `selling_general_and_administrative_expenses`, `exploration_expenses`, `depreciation_depletion_and_amortization`, `taxes_other_than_income`, `interest_and_debt_expense`, `other_net_periodic_benefit_costs`, `nci`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_and_other_operating_revenues_yoy` | `sales_and_other_operating_revenues` | Yıllık büyüme | Sales and other operating revenues YoY growth rate vs Q-4 |
| `purchased_crude_oil_and_products_margin_delta_bps` | `purchased_crude_oil_and_products / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Purchased crude oil and products as % of total revenues and other income, delta vs Q-4 |
| `operating_expenses_margin_delta_bps` | `operating_expenses / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Operating expenses as % of total revenues and other income, delta vs Q-4 |
| `selling_general_and_administrative_expenses_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Selling, general and administrative expenses as % of total revenues and other income, delta vs Q-4 |
| `exploration_expenses_yoy` | `exploration_expenses` | Yıllık büyüme | Exploration expenses YoY growth rate vs Q-4 |
| `depreciation_depletion_and_amortization_margin_delta_bps` | `depreciation_depletion_and_amortization / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Depreciation, depletion and amortization as % of total revenues and other income, delta vs Q-4 |
| `income_from_equity_affiliates_yoy` | `income_from_equity_affiliates` | Yıllık büyüme | income_from_equity_affiliates YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `taxes_other_than_income_yoy` | `taxes_other_than_income` | Yıllık büyüme | taxes_other_than_income YoY growth rate vs Q-4 |
| `interest_and_debt_expense_yoy` | `interest_and_debt_expense` | Yıllık büyüme | interest_and_debt_expense YoY growth rate vs Q-4 |
| `other_net_periodic_benefit_costs_yoy` | `other_net_periodic_benefit_costs` | Yıllık büyüme | other_net_periodic_benefit_costs YoY growth rate vs Q-4 |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## CVX_2026Q1

Geçmiş dayanak kalemleri: `sales_and_other_operating_revenues`, `income_from_equity_affiliates`, `other_income`, `purchased_crude_oil_and_products`, `operating_expenses`, `sga`, `exploration_expenses`, `depreciation_depletion_amortization`, `taxes_other_than_on_income`, `interest_and_debt_expense`, `other_components_of_net_periodic_benefit_costs`, `nci`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_revenue_yoy` | `sales_and_other_operating_revenues` | Yıllık büyüme | Sales and other operating revenues YoY growth vs Q-4 |
| `equity_income_yoy` | `income_from_equity_affiliates` | Yıllık büyüme | Equity affiliate income YoY growth vs Q-4 |
| `other_income_yoy` | `other_income` | Yıllık büyüme | Other income YoY growth vs Q-4 |
| `purchased_crude_margin_delta_bps` | `purchased_crude_oil_and_products / çapa: total_revenue` | Marj değişimi, baz puan | Purchased crude oil and products as % of total revenue, delta vs Q-4 |
| `opex_yoy` | `total_opex` | Yıllık büyüme | Total operating and SG&A expenses YoY growth vs Q-4 |
| `dd_and_a_yoy` | `depreciation_depletion_amortization` | Yıllık büyüme | Depreciation, depletion and amortization YoY growth vs Q-4 |
| `exploration_expenses_yoy` | `exploration_expenses` | Yıllık büyüme | exploration_expenses YoY growth rate vs Q-4 |
| `taxes_other_than_on_income_yoy` | `taxes_other_than_on_income` | Yıllık büyüme | taxes_other_than_on_income YoY growth rate vs Q-4 |
| `interest_and_debt_expense_yoy` | `interest_and_debt_expense` | Yıllık büyüme | interest_and_debt_expense YoY growth rate vs Q-4 |
| `other_components_of_net_periodic_benefit_costs_yoy` | `other_components_of_net_periodic_benefit_costs` | Yıllık büyüme | other_components_of_net_periodic_benefit_costs YoY growth rate vs Q-4 |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## C_2025Q4

Geçmiş dayanak kalemleri: `total_revenues`, `total_provisions`, `total_operating_expenses`, `noncontrolling_interests`, `discontinued_ops_loss`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `total_revenues_yoy` | `total_revenues` | Yıllık büyüme | Total revenue (net interest + non-interest) YoY growth rate vs Q-4 |
| `provisions_margin_delta_bps` | `total_provisions / çapa: total_revenues` | Marj değişimi, baz puan | Total provisions as % of total revenue, delta vs Q-4 |
| `opex_margin_delta_bps` | `total_operating_expenses / çapa: total_revenues` | Marj değişimi, baz puan | Total operating expenses as % of total revenue, delta vs Q-4 |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `discontinued_ops_loss_abs` | `discontinued_ops_loss` | Doğrudan tutar veya adet | discontinued_ops_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## C_2026Q1

Geçmiş dayanak kalemleri: `interest_income`, `interest_expense`, `commissions_and_fees`, `principal_transactions`, `administration_and_other_fiduciary_fees`, `realized_gains_on_sales_of_investments_net`, `impairment_losses_on_investments`, `other_revenue_reduction`, `provision_for_credit_losses_on_loans`, `release_for_credit_losses_on_htm_debt_securities`, `provision_for_credit_losses_on_other_assets`, `policyholder_benefits_and_claims`, `provision_for_credit_losses_on_unfunded_lending_commitments`, `compensation_and_benefits`, `technology_communication`, `transactional_and_tax_charges`, `premises_and_equipment`, `professional_services`, `advertising_and_marketing`, `restructuring_benefit`, `other_operating`, `loss_from_discontinued_operations_net`, `noncontrolling_interests`, `preferred_stock_dividends`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_interest_income_yoy` | `net_interest_income` | Yıllık büyüme | Net interest income YoY growth rate vs Q-4 |
| `non_interest_revenues_yoy` | `non_interest_revenues` | Yıllık büyüme | Non-interest revenues YoY growth rate vs Q-4 |
| `provisions_margin_delta_bps` | `total_provisions / çapa: total_revenues` | Marj değişimi, baz puan | Total provisions for credit losses and benefits as % of total revenues, delta vs Q-4 |
| `operating_expenses_yoy` | `total_operating_expenses` | Yıllık büyüme | Total operating expenses YoY growth rate vs Q-4 |
| `loss_from_discontinued_operations_net_abs` | `loss_from_discontinued_operations_net` | Doğrudan tutar veya adet | loss_from_discontinued_operations_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## DAL_2025Q4

Geçmiş dayanak kalemleri: `passenger_revenue`, `cargo_revenue`, `other_revenue`, `salaries_and_related_costs`, `aircraft_fuel_and_related_taxes`, `ancillary_businesses_and_refinery`, `contracted_services`, `landing_fees_and_other_rents`, `aircraft_maintenance_materials_and_outside_repairs`, `depreciation_and_amortization`, `passenger_commissions_and_other_selling_expenses`, `regional_carrier_expense`, `passenger_service`, `profit_sharing`, `aircraft_rent`, `pilot_agreement_and_related_expenses`, `other_operating_expense`, `total_non_operating_expense_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_revenue_yoy` | `passenger_revenue` | Yıllık büyüme | Passenger revenue YoY growth rate vs Q-4 |
| `cargo_revenue_yoy` | `cargo_revenue` | Yıllık büyüme | Cargo revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `salaries_and_related_costs_margin_delta_bps` | `salaries_and_related_costs / çapa: total_operating_revenue` | Marj değişimi, baz puan | Salaries and related costs as % of total operating revenue, delta vs Q-4 |
| `aircraft_fuel_and_related_taxes_margin_delta_bps` | `aircraft_fuel_and_related_taxes / çapa: total_operating_revenue` | Marj değişimi, baz puan | Aircraft fuel and related taxes as % of total operating revenue, delta vs Q-4 |
| `total_non_operating_expense_net_margin_delta_bps` | `total_non_operating_expense_net / çapa: total_operating_revenue` | Marj değişimi, baz puan | Total non-operating expense as % of total operating revenue, delta vs Q-4 |
| `ancillary_businesses_and_refinery_yoy` | `ancillary_businesses_and_refinery` | Yıllık büyüme | ancillary_businesses_and_refinery YoY growth rate vs Q-4 |
| `contracted_services_yoy` | `contracted_services` | Yıllık büyüme | contracted_services YoY growth rate vs Q-4 |
| `landing_fees_and_other_rents_yoy` | `landing_fees_and_other_rents` | Yıllık büyüme | landing_fees_and_other_rents YoY growth rate vs Q-4 |
| `aircraft_maintenance_materials_and_outside_repairs_yoy` | `aircraft_maintenance_materials_and_outside_repairs` | Yıllık büyüme | aircraft_maintenance_materials_and_outside_repairs YoY growth rate vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `passenger_commissions_and_other_selling_expenses_yoy` | `passenger_commissions_and_other_selling_expenses` | Yıllık büyüme | passenger_commissions_and_other_selling_expenses YoY growth rate vs Q-4 |
| `regional_carrier_expense_yoy` | `regional_carrier_expense` | Yıllık büyüme | regional_carrier_expense YoY growth rate vs Q-4 |
| `passenger_service_yoy` | `passenger_service` | Yıllık büyüme | passenger_service YoY growth rate vs Q-4 |
| `profit_sharing_yoy` | `profit_sharing` | Yıllık büyüme | profit_sharing YoY growth rate vs Q-4 |
| `aircraft_rent_yoy` | `aircraft_rent` | Yıllık büyüme | aircraft_rent YoY growth rate vs Q-4 |
| `pilot_agreement_and_related_expenses_abs` | `pilot_agreement_and_related_expenses` | Doğrudan tutar veya adet | pilot_agreement_and_related_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_operating_expense_abs` | `other_operating_expense` | Doğrudan tutar veya adet | other_operating_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## DAL_2026Q1

Geçmiş dayanak kalemleri: `passenger_revenue`, `cargo_revenue`, `other_revenue`, `salaries_and_related_costs`, `aircraft_fuel_and_related_taxes`, `ancillary_businesses_and_refinery`, `contracted_services`, `landing_fees_and_other_rents`, `aircraft_maintenance_materials_and_outside_repairs`, `regional_carrier_expense`, `depreciation_and_amortization`, `passenger_commissions_and_other_selling_expenses`, `passenger_service`, `aircraft_rent`, `profit_sharing`, `other_operating_expense`, `interest_expense_net`, `investment_losses_net`, `loss_on_extinguishment_of_debt`, `miscellaneous_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_revenue_yoy` | `passenger_revenue` | Yıllık büyüme | Passenger revenue YoY growth rate vs Q-4 |
| `cargo_revenue_yoy` | `cargo_revenue` | Yıllık büyüme | Cargo revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `total_opex_margin_delta_bps` | `total_operating_expense / çapa: total_revenue` | Marj değişimi, baz puan | Total operating expense as a percentage of total revenue, delta vs Q-4 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `investment_losses_net_abs` | `investment_losses_net` | Doğrudan tutar veya adet | investment_losses_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_on_extinguishment_of_debt_abs` | `loss_on_extinguishment_of_debt` | Doğrudan tutar veya adet | loss_on_extinguishment_of_debt absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `miscellaneous_net_yoy` | `miscellaneous_net` | Yıllık büyüme | miscellaneous_net YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## DELL_2026Q4

Geçmiş dayanak kalemleri: `products_revenue`, `services_revenue`, `products_cogs`, `services_cogs`, `sga`, `rd`, `interest_and_other_net`, `net_loss_nci`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Products revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `interest_and_other_net_yoy` | `interest_and_other_net` | Yıllık büyüme | interest_and_other_net YoY growth rate vs Q-4 |
| `net_loss_nci_abs` | `net_loss_nci` | Doğrudan tutar veya adet | net_loss_nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## DELL_2027Q1

Geçmiş dayanak kalemleri: `products_revenue`, `services_revenue`, `products_cogs`, `services_cogs`, `sga`, `rd`, `interest_and_other_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Products revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of revenue as % of total net revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total net revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `interest_and_other_net_yoy` | `interest_and_other_net` | Yıllık büyüme | interest_and_other_net YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## DIS_2026Q1

Geçmiş dayanak kalemleri: `services`, `products`, `cost_services`, `cost_products`, `sga`, `depreciation_amortization`, `restructuring_impairment`, `interest_expense_net`, `equity_income`, `nci`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `services_revenue_yoy` | `services` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `products_revenue_yoy` | `products` | Yıllık büyüme | Products revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `depreciation_amortization_yoy` | `depreciation_amortization` | Yıllık büyüme | depreciation_amortization YoY growth rate vs Q-4 |
| `restructuring_impairment_abs` | `restructuring_impairment` | Doğrudan tutar veya adet | restructuring_impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `equity_income_abs` | `equity_income` | Doğrudan tutar veya adet | equity_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## GE_2025Q4

Geçmiş dayanak kalemleri: `equipment_revenue`, `services_revenue`, `insurance_revenue`, `cost_equipment_sold`, `cost_services_sold`, `sga`, `separation_costs`, `rd`, `interest_and_other_financial_charges`, `insurance_losses_and_other_costs`, `goodwill_impairments`, `non_operating_benefit_income`, `other_income`, `nci`, `preferred_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `equipment_revenue_yoy` | `equipment_revenue` | Yıllık büyüme | Equipment revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `insurance_revenue_yoy` | `insurance_revenue` | Yıllık büyüme | Insurance revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `separation_costs_yoy` | `separation_costs` | Yıllık büyüme | Separation costs YoY growth rate vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `interest_charges_yoy` | `interest_and_other_financial_charges` | Yıllık büyüme | Interest and other financial charges YoY growth rate vs Q-4 |
| `insurance_losses_yoy` | `insurance_losses_and_other_costs` | Yıllık büyüme | Insurance losses, annuity benefits and other costs YoY growth rate vs Q-4 |
| `other_income_yoy` | `other_income` | Yıllık büyüme | Other income (loss) YoY growth rate vs Q-4 |
| `goodwill_impairments_abs` | `goodwill_impairments` | Doğrudan tutar veya adet | goodwill_impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `non_operating_benefit_income_abs` | `non_operating_benefit_income` | Doğrudan tutar veya adet | non_operating_benefit_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_dividends_abs` | `preferred_dividends` | Doğrudan tutar veya adet | preferred_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## GE_2026Q1

Geçmiş dayanak kalemleri: `sales_of_equipment`, `sales_of_services`, `insurance_revenue`, `cost_of_equipment_sold`, `cost_of_services_sold`, `sga`, `separation_costs`, `rd`, `interest_and_other_financial_charges`, `insurance_losses_annuity_benefits_and_other_costs`, `non_operating_benefit_income`, `other_income`, `tax_rate`, `discontinued_operations_net`, `noncontrolling_interest`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `equipment_revenue_yoy` | `sales_of_equipment` | Yıllık büyüme | Sales of equipment YoY growth rate vs Q-4 baseline |
| `services_revenue_yoy` | `sales_of_services` | Yıllık büyüme | Sales of services YoY growth rate vs Q-4 baseline |
| `insurance_revenue_yoy` | `insurance_revenue` | Yıllık büyüme | Insurance revenue YoY growth rate vs Q-4 baseline |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of sales as a percentage of total revenue, delta vs Q-4 baseline |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 baseline |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 baseline |
| `separation_costs_abs` | `separation_costs` | Doğrudan tutar veya adet | separation_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_other_financial_charges_yoy` | `interest_and_other_financial_charges` | Yıllık büyüme | interest_and_other_financial_charges YoY growth rate vs Q-4 |
| `insurance_losses_annuity_benefits_and_other_costs_abs` | `insurance_losses_annuity_benefits_and_other_costs` | Doğrudan tutar veya adet | insurance_losses_annuity_benefits_and_other_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `non_operating_benefit_income_abs` | `non_operating_benefit_income` | Doğrudan tutar veya adet | non_operating_benefit_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `discontinued_operations_net_abs` | `discontinued_operations_net` | Doğrudan tutar veya adet | discontinued_operations_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## GM_2025Q4

Geçmiş dayanak kalemleri: `automotive_revenue`, `gm_financial_revenue`, `automotive_cos`, `gm_financial_expenses`, `automotive_sga`, `automotive_interest_expense`, `interest_income_net`, `equity_loss`, `nci_income`, `preferred_redemption_gain`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `automotive_revenue_yoy` | `automotive_revenue` | Yıllık büyüme | Automotive revenue YoY growth rate vs Q-4 |
| `gm_financial_revenue_yoy` | `gm_financial_revenue` | Yıllık büyüme | GM Financial revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `automotive_sga / çapa: total_revenue` | Marj değişimi, baz puan | Automotive SG&A as % of total revenue, delta vs Q-4 |
| `automotive_interest_expense_yoy` | `automotive_interest_expense` | Yıllık büyüme | automotive_interest_expense YoY growth rate vs Q-4 |
| `interest_income_net_yoy` | `interest_income_net` | Yıllık büyüme | interest_income_net YoY growth rate vs Q-4 |
| `equity_loss_abs` | `equity_loss` | Doğrudan tutar veya adet | equity_loss absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_income_abs` | `nci_income` | Doğrudan tutar veya adet | nci_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_redemption_gain_abs` | `preferred_redemption_gain` | Doğrudan tutar veya adet | preferred_redemption_gain absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## GOOGL_2026Q1

Geçmiş dayanak kalemleri: `revenues`, `cost_of_revenues`, `research_and_development`, `sales_and_marketing`, `general_and_administrative`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenues_yoy` | `revenues` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenues / çapa: revenues` | Marj değişimi, baz puan | Cost of revenues as a percentage of total revenue, delta vs Q-4 |
| `rd_yoy` | `research_and_development` | Yıllık büyüme | Research and development expense YoY growth rate vs Q-4 |
| `sales_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `general_admin_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## GS_2025Q4

Geçmiş dayanak kalemleri: `investment_banking`, `investment_management`, `commissions_and_fees`, `market_making`, `other_principal_transactions`, `interest_income`, `interest_expense`, `provision_for_credit_losses`, `compensation_and_benefits`, `transaction_based`, `market_development`, `communications_and_technology`, `depreciation_and_amortization`, `occupancy`, `professional_fees`, `other_expenses`, `preferred_stock_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `investment_banking_yoy` | `investment_banking` | Yıllık büyüme | Investment banking revenue YoY growth rate vs Q-4 |
| `investment_management_yoy` | `investment_management` | Yıllık büyüme | Investment management revenue YoY growth rate vs Q-4 |
| `commissions_and_fees_yoy` | `commissions_and_fees` | Yıllık büyüme | Commissions and fees revenue YoY growth rate vs Q-4 |
| `market_making_yoy` | `market_making` | Yıllık büyüme | Market making revenue YoY growth rate vs Q-4 |
| `other_principal_transactions_yoy` | `other_principal_transactions` | Yıllık büyüme | Other principal transactions revenue YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `provision_for_credit_losses_yoy` | `provision_for_credit_losses` | Yıllık büyüme | provision_for_credit_losses YoY growth rate vs Q-4 |
| `compensation_and_benefits_yoy` | `compensation_and_benefits` | Yıllık büyüme | compensation_and_benefits YoY growth rate vs Q-4 |
| `transaction_based_yoy` | `transaction_based` | Yıllık büyüme | transaction_based YoY growth rate vs Q-4 |
| `market_development_yoy` | `market_development` | Yıllık büyüme | market_development YoY growth rate vs Q-4 |
| `communications_and_technology_yoy` | `communications_and_technology` | Yıllık büyüme | communications_and_technology YoY growth rate vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `occupancy_yoy` | `occupancy` | Yıllık büyüme | occupancy YoY growth rate vs Q-4 |
| `professional_fees_yoy` | `professional_fees` | Yıllık büyüme | professional_fees YoY growth rate vs Q-4 |
| `other_expenses_abs` | `other_expenses` | Doğrudan tutar veya adet | other_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## GS_2026Q1

Geçmiş dayanak kalemleri: `investment_banking`, `investment_management`, `commissions_and_fees`, `market_making`, `other_principal_transactions`, `interest_income`, `interest_expense`, `provision_for_credit_losses`, `compensation_and_benefits`, `transaction_based`, `market_development`, `communications_and_technology`, `depreciation_and_amortization`, `occupancy`, `professional_fees`, `other_expenses`, `tax_rate`, `preferred_stock_dividends`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `investment_banking_yoy` | `investment_banking` | Yıllık büyüme | Investment banking revenue YoY growth rate vs Q-4 |
| `investment_management_yoy` | `investment_management` | Yıllık büyüme | Investment management revenue YoY growth rate vs Q-4 |
| `commissions_and_fees_yoy` | `commissions_and_fees` | Yıllık büyüme | Commissions and fees revenue YoY growth rate vs Q-4 |
| `trading_revenue_yoy` | `trading_revenue` | Yıllık büyüme | Combined market making and other principal transactions revenue YoY growth rate vs Q-4 |
| `net_interest_margin_delta_bps` | `net_interest_income / çapa: total_net_revenues` | Marj değişimi, baz puan | Net interest income (interest income minus interest expense) as % of total net revenues, delta vs Q-4 |
| `total_operating_expenses_margin_delta_bps` | `total_operating_expenses / çapa: total_net_revenues` | Marj değişimi, baz puan | Total operating expenses as % of total net revenues, delta vs Q-4 |
| `provision_for_credit_losses_abs` | `provision_for_credit_losses` | Doğrudan tutar veya adet | provision_for_credit_losses absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## HD_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `sg_and_a`, `depreciation_and_amortization`, `interest_income_and_other_net`, `interest_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as % of net sales, delta vs Q-4 |
| `sg_and_a_margin_delta_bps` | `sg_and_a / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of net sales, delta vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | Depreciation and amortization expense YoY growth rate vs Q-4 |
| `interest_income_and_other_net_abs` | `interest_income_and_other_net` | Doğrudan tutar veya adet | interest_income_and_other_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## HON_2025Q4

Geçmiş dayanak kalemleri: `product_sales`, `service_sales`, `net_sales`, `cost_of_products_sold`, `cost_of_services_sold`, `total_cost_of_products_and_services_sold`, `rd`, `sga`, `impairment_of_assets_held_for_sale`, `other_income_net`, `interest_and_other_financial_charges`, `total_costs_expenses_and_other`, `income_before_taxes`, `net_income`, `net_income_noncontrolling_interest`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_sales_yoy` | `product_sales` | Yıllık büyüme | Product sales YoY growth rate vs Q-4 |
| `service_sales_yoy` | `service_sales` | Yıllık büyüme | Service sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cost_of_products_and_services_sold / çapa: net_sales` | Marj değişimi, baz puan | Combined cost of products and services sold as % of net sales, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expenses YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | SG&A expenses as % of net sales, delta vs Q-4 |
| `impairment_of_assets_held_for_sale_abs` | `impairment_of_assets_held_for_sale` | Doğrudan tutar veya adet | impairment_of_assets_held_for_sale absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_other_financial_charges_yoy` | `interest_and_other_financial_charges` | Yıllık büyüme | interest_and_other_financial_charges YoY growth rate vs Q-4 |
| `income_before_taxes_abs` | `income_before_taxes` | Doğrudan tutar veya adet | income_before_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_income_noncontrolling_interest_abs` | `net_income_noncontrolling_interest` | Doğrudan tutar veya adet | net_income_noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## HON_2026Q1

Geçmiş dayanak kalemleri: `product_sales`, `service_sales`, `cost_of_products_sold`, `cost_of_services_sold`, `rd`, `sga`, `impairment_of_assets_held_for_sale`, `other_income`, `interest_and_other_financial_charges`, `tax_rate`, `noncontrolling_interest`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_sales_yoy` | `product_sales` | Yıllık büyüme | Product sales YoY growth rate vs 2025Q1 |
| `service_sales_yoy` | `service_sales` | Yıllık büyüme | Service sales YoY growth rate vs 2025Q1 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: net_sales` | Marj değişimi, baz puan | COGS as % of net sales, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs 2025Q1 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | SG&A as % of net sales, delta vs Q-4 |
| `impairment_of_assets_held_for_sale_abs` | `impairment_of_assets_held_for_sale` | Doğrudan tutar veya adet | impairment_of_assets_held_for_sale absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_other_financial_charges_yoy` | `interest_and_other_financial_charges` | Yıllık büyüme | interest_and_other_financial_charges YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## HOOD_2025Q4

Geçmiş dayanak kalemleri: `transaction_revenue`, `net_interest_revenue`, `other_revenue`, `brokerage_and_transaction`, `technology_and_development`, `operations`, `provision_for_credit_losses`, `marketing`, `general_and_administrative`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `transaction_revenue_yoy` | `transaction_revenue` | Yıllık büyüme | Transaction-based revenue YoY growth rate vs Q-4 |
| `net_interest_revenue_yoy` | `net_interest_revenue` | Yıllık büyüme | Net interest revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `total_opex_margin_delta_bps` | `total_opex / çapa: total_revenue` | Marj değişimi, baz puan | Total operating expenses as % of total revenue, delta vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## HOOD_2026Q1

Geçmiş dayanak kalemleri: `transaction_based_revenues`, `net_interest_revenues`, `other_revenues`, `brokerage_and_transaction`, `technology_and_development`, `operations`, `provision_for_credit_losses`, `marketing`, `general_and_administrative`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `transaction_based_revenues_yoy` | `transaction_based_revenues` | Yıllık büyüme | Transaction-based revenues YoY growth rate vs Q-4 |
| `net_interest_revenues_yoy` | `net_interest_revenues` | Yıllık büyüme | Net interest revenues YoY growth rate vs Q-4 |
| `other_revenues_yoy` | `other_revenues` | Yıllık büyüme | Other revenues YoY growth rate vs Q-4 |
| `operating_expenses_margin_delta_bps` | `total_operating_expenses / çapa: total_revenues` | Marj değişimi, baz puan | Total operating expenses as a percentage of total revenues, delta vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## IBM_2026Q1

Geçmiş dayanak kalemleri: `services_revenue`, `sales_revenue`, `financing_revenue`, `services_cost`, `sales_cost`, `financing_cost`, `sga`, `rd`, `ip_and_custom_development_income`, `other_income`, `interest_expense`, `tax_rate`, `discontinued_operations_net`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `sales_revenue_yoy` | `sales_revenue` | Yıllık büyüme | Sales revenue YoY growth rate vs Q-4 |
| `cost_margin_delta_bps` | `total_cost / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `financing_revenue_yoy` | `financing_revenue` | Yıllık büyüme | financing_revenue YoY growth rate vs Q-4 |
| `ip_and_custom_development_income_yoy` | `ip_and_custom_development_income` | Yıllık büyüme | ip_and_custom_development_income YoY growth rate vs Q-4 |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `discontinued_operations_net_abs` | `discontinued_operations_net` | Doğrudan tutar veya adet | discontinued_operations_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## INTC_2025Q4

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_sales`, `research_and_development`, `marketing_general_and_administrative`, `restructuring_and_other_charges`, `gains_losses_on_equity_investments_net`, `interest_and_other_net`, `nci`, `shares`, `tax_provision`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `marketing_general_and_administrative_margin_delta_bps` | `marketing_general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | MG&A expense as % of total revenue, delta vs Q-4 |
| `restructuring_and_other_charges_abs` | `restructuring_and_other_charges` | Doğrudan tutar veya adet | restructuring_and_other_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `gains_losses_on_equity_investments_net_abs` | `gains_losses_on_equity_investments_net` | Doğrudan tutar veya adet | gains_losses_on_equity_investments_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_and_other_net_abs` | `interest_and_other_net` | Doğrudan tutar veya adet | interest_and_other_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_amount` | `tax_provision` | Doğrudan tutar veya adet | Income tax provision/expense for the target quarter, in DOLLARS (same units as the Q-4 baseline) — NOT a rate. Pretax income is near zero or negative this quarter, which makes an effective tax RATE numerically meaningless (a small pretax swing produces an enormous rate swing). Predict the dollar tax provision directly; sign matters (a tax BENEFIT is negative). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## INTU_2026Q2

Geçmiş dayanak kalemleri: `service_revenue`, `product_and_other_revenue`, `cost_of_service_revenue`, `cost_of_product_and_other_revenue`, `amortization_of_acquired_technology`, `selling_and_marketing`, `research_and_development`, `general_and_administrative`, `amortization_of_other_acquired_intangible_assets`, `restructuring`, `interest_expense`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `service_revenue_yoy` | `service_revenue` | Yıllık büyüme | Service revenue YoY growth rate vs Q-4 |
| `product_and_other_revenue_yoy` | `product_and_other_revenue` | Yıllık büyüme | Product and other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cost_of_revenue / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of revenue as % of total revenue, delta vs Q-4 |
| `selling_and_marketing_margin_delta_bps` | `selling_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Selling and marketing as % of total revenue, delta vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: total_revenue` | Marj değişimi, baz puan | G&A as % of total revenue, delta vs Q-4 |
| `amortization_of_other_acquired_intangible_assets_yoy` | `amortization_of_other_acquired_intangible_assets` | Yıllık büyüme | amortization_of_other_acquired_intangible_assets YoY growth rate vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## INTU_2026Q3

Geçmiş dayanak kalemleri: `service_revenue`, `product_and_other_revenue`, `cost_of_service_revenue`, `cost_of_product_and_other_revenue`, `amortization_of_acquired_technology`, `selling_and_marketing`, `rd`, `general_and_administrative`, `amortization_of_other_acquired_intangible_assets`, `restructuring`, `interest_expense`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `service_revenue_yoy` | `service_revenue` | Yıllık büyüme | Service revenue YoY growth rate vs Q-4 baseline |
| `product_and_other_revenue_yoy` | `product_and_other_revenue` | Yıllık büyüme | Product and other revenue YoY growth rate vs Q-4 baseline |
| `cost_of_revenue_margin_delta_bps` | `cost_of_revenue / çapa: total_revenue` | Marj değişimi, baz puan | Cost of revenue as % of total revenue, delta vs Q-4 |
| `selling_and_marketing_yoy` | `selling_and_marketing` | Yıllık büyüme | Selling and marketing expense YoY growth rate vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | Research and development expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `amortization_of_other_acquired_intangible_assets_yoy` | `amortization_of_other_acquired_intangible_assets` | Yıllık büyüme | amortization_of_other_acquired_intangible_assets YoY growth rate vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## ISRG_2025Q4

Geçmiş dayanak kalemleri: `product_revenue`, `service_revenue`, `product_cogs`, `service_cogs`, `sga`, `rd`, `other_income_net`, `tax_rate`, `shares`, `nci`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `service_revenue_yoy` | `service_revenue` | Yıllık büyüme | Service revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## JNJ_2025Q4

Geçmiş dayanak kalemleri: `sales_to_customers`, `cost_of_products_sold`, `selling_marketing_administrative_expenses`, `research_and_development_expense`, `in_process_research_and_development_impairments`, `interest_income`, `interest_expense`, `other_income_expense_net`, `restructuring`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_to_customers_yoy` | `sales_to_customers` | Yıllık büyüme | Customer sales YoY growth rate vs Q-4 |
| `cost_of_products_sold_margin_delta_bps` | `cost_of_products_sold / çapa: sales_to_customers` | Marj değişimi, baz puan | COGS as % of sales, delta vs Q-4 |
| `research_and_development_expense_yoy` | `research_and_development_expense` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `selling_marketing_administrative_expenses_yoy` | `selling_marketing_administrative_expenses` | Yıllık büyüme | Selling, marketing and administrative expense YoY growth rate vs Q-4 |
| `in_process_research_and_development_impairments_abs` | `in_process_research_and_development_impairments` | Doğrudan tutar veya adet | in_process_research_and_development_impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_abs` | `interest_income` | Doğrudan tutar veya adet | interest_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## JNJ_2026Q1

Geçmiş dayanak kalemleri: `sales_to_customers`, `cost_of_products_sold`, `sga`, `rd`, `restructuring`, `interest_income`, `interest_expense_net`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_yoy` | `sales_to_customers` | Yıllık büyüme | Sales to customers YoY growth vs 2025Q1 baseline |
| `cogs_margin_delta_bps` | `cost_of_products_sold / çapa: sales_to_customers` | Marj değişimi, baz puan | Cost of products sold as % of sales, delta vs 2025Q1 baseline |
| `sga_margin_delta_bps` | `sga / çapa: sales_to_customers` | Marj değişimi, baz puan | SG&A as % of sales, delta vs 2025Q1 baseline |
| `rd_margin_delta_bps` | `rd / çapa: sales_to_customers` | Marj değişimi, baz puan | R&D as % of sales, delta vs 2025Q1 baseline |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## JPM_2025Q4

Geçmiş dayanak kalemleri: `investment_banking_fees`, `principal_transactions`, `lending_deposit_fees`, `asset_management_fees`, `commissions_other_fees`, `investment_securities_losses`, `mortgage_fees`, `card_income`, `other_income`, `interest_income`, `interest_expense`, `provision_for_credit_losses`, `compensation_expense`, `occupancy_expense`, `tech_communications_equipment_expense`, `professional_outside_services`, `marketing_expense`, `other_expense`, `preferred_dividends`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `noninterest_revenue_yoy` | `noninterest_revenue` | Yıllık büyüme | Noninterest revenue YoY growth rate vs Q-4 |
| `net_interest_income_yoy` | `net_interest_income` | Yıllık büyüme | Net interest income YoY growth rate vs Q-4 |
| `provision_margin_delta_bps` | `provision_for_credit_losses / çapa: total_net_revenue` | Marj değişimi, baz puan | Provision for credit losses as % of total net revenue, delta vs Q-4 |
| `compensation_expense_yoy` | `compensation_expense` | Yıllık büyüme | Compensation expense YoY growth rate vs Q-4 |
| `other_operating_expense_margin_delta_bps` | `other_operating_expense / çapa: total_net_revenue` | Marj değişimi, baz puan | Other operating expenses (excluding compensation) as % of total net revenue, delta vs Q-4 |
| `preferred_dividends_abs` | `preferred_dividends` | Doğrudan tutar veya adet | preferred_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## JPM_2026Q1

Geçmiş dayanak kalemleri: `investment_banking_fees`, `principal_transactions`, `lending_deposit_fees`, `asset_management_fees`, `commissions_and_other_fees`, `investment_securities_losses`, `mortgage_fees_and_related_income`, `card_income`, `other_income`, `interest_income`, `interest_expense`, `provision_for_credit_losses`, `compensation_expense`, `occupancy_expense`, `technology_communications_equipment_expense`, `professional_and_outside_services`, `marketing_expense`, `other_expense`, `tax_rate`, `preferred_stock_dividends`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `noninterest_revenue_yoy` | `noninterest_revenue` | Yıllık büyüme | Noninterest revenue YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | Interest income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | Interest expense YoY growth rate vs Q-4 |
| `provision_for_credit_losses_margin_delta_bps` | `provision_for_credit_losses / çapa: total_net_revenue` | Marj değişimi, baz puan | Provision for credit losses as % of total net revenue, delta vs Q-4 |
| `compensation_expense_margin_delta_bps` | `compensation_expense / çapa: total_net_revenue` | Marj değişimi, baz puan | Compensation expense as % of total net revenue, delta vs Q-4 |
| `noncomp_expense_margin_delta_bps` | `noncomp_expense / çapa: total_net_revenue` | Marj değişimi, baz puan | Non-compensation noninterest expense as % of total net revenue, delta vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## KHC_2025Q4

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_products_sold`, `selling_general_and_administrative_excluding_impairment`, `goodwill_impairment_losses`, `intangible_asset_impairment_losses`, `interest_expense`, `other_income_net`, `noncontrolling_interest`, `shares`, `tax_provision`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cost_of_products_sold_margin_delta_bps` | `cost_of_products_sold / çapa: net_sales` | Marj değişimi, baz puan | Cost of products sold as % of net sales, delta vs Q-4 |
| `selling_general_and_administrative_excluding_impairment_yoy` | `selling_general_and_administrative_excluding_impairment` | Yıllık büyüme | SG&A excluding impairment losses YoY growth rate vs Q-4 |
| `goodwill_impairment_losses_yoy` | `goodwill_impairment_losses` | Yıllık büyüme | Goodwill impairment losses YoY growth rate vs Q-4 |
| `intangible_asset_impairment_losses_yoy` | `intangible_asset_impairment_losses` | Yıllık büyüme | Intangible asset impairment losses YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | Interest expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_amount` | `tax_provision` | Doğrudan tutar veya adet | Income tax provision/expense for the target quarter, in DOLLARS (same units as the Q-4 baseline) — NOT a rate. Pretax income is near zero or negative this quarter, which makes an effective tax RATE numerically meaningless (a small pretax swing produces an enormous rate swing). Predict the dollar tax provision directly; sign matters (a tax BENEFIT is negative). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## KHC_2026Q1

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_products_sold`, `sga`, `interest_expense`, `other_income_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_products_sold / çapa: net_sales` | Marj değişimi, baz puan | Cost of products sold as % of net sales, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | SG&A expense as % of net sales, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | Interest expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## KO_2025Q4

Geçmiş dayanak kalemleri: `net_operating_revenues`, `cost_of_goods_sold`, `selling_general_and_administrative_expenses`, `other_operating_charges`, `interest_income`, `interest_expense`, `equity_income_net`, `other_income_net`, `net_income_attributable_to_noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_operating_revenues_yoy` | `net_operating_revenues` | Yıllık büyüme | Operating revenue YoY growth rate vs 2024Q4 |
| `cost_of_goods_sold_margin_delta_bps` | `cost_of_goods_sold / çapa: net_operating_revenues` | Marj değişimi, baz puan | COGS as a percentage of operating revenues, delta vs 2024Q4 |
| `selling_general_and_administrative_expenses_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: net_operating_revenues` | Marj değişimi, baz puan | SG&A as a percentage of operating revenues, delta vs 2024Q4 |
| `other_operating_charges_yoy` | `other_operating_charges` | Yıllık büyüme | Other operating charges YoY growth rate vs 2024Q4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `equity_income_net_abs` | `equity_income_net` | Doğrudan tutar veya adet | equity_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## KO_2026Q1

Geçmiş dayanak kalemleri: `net_operating_revenues`, `cost_of_goods_sold`, `selling_general_and_administrative`, `other_operating_charges`, `interest_income`, `interest_expense`, `equity_income_net`, `other_income_net`, `income_taxes`, `noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `net_operating_revenues` | Yıllık büyüme | Net operating revenues YoY growth rate vs 2025Q1 |
| `cogs_margin_delta_bps` | `cost_of_goods_sold / çapa: net_operating_revenues` | Marj değişimi, baz puan | Cost of goods sold as % of net operating revenues, delta vs 2025Q1 |
| `sga_margin_delta_bps` | `selling_general_and_administrative / çapa: net_operating_revenues` | Marj değişimi, baz puan | SG&A as % of net operating revenues, delta vs 2025Q1 |
| `other_operating_charges_yoy` | `other_operating_charges` | Yıllık büyüme | Other operating charges YoY growth rate vs 2025Q1 |
| `income_taxes_yoy` | `income_taxes` | Yıllık büyüme | Income taxes YoY growth rate vs 2025Q1 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `equity_income_net_abs` | `equity_income_net` | Doğrudan tutar veya adet | equity_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## LLY_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `rd`, `msa`, `acquired_in_process_rd`, `asset_impairment_restructuring_and_other_special_charges`, `other_net_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs 2025Q1 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as % of revenue, delta vs 2025Q1 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs 2025Q1 |
| `msa_yoy` | `msa` | Yıllık büyüme | Marketing, selling, and administrative expense YoY growth rate vs 2025Q1 |
| `acquired_in_process_rd_abs` | `acquired_in_process_rd` | Doğrudan tutar veya adet | acquired_in_process_rd absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `asset_impairment_restructuring_and_other_special_charges_abs` | `asset_impairment_restructuring_and_other_special_charges` | Doğrudan tutar veya adet | asset_impairment_restructuring_and_other_special_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_net_expense_yoy` | `other_net_expense` | Yıllık büyüme | other_net_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## LMT_2025Q4

Geçmiş dayanak kalemleri: `products_revenue`, `services_revenue`, `products_cogs`, `services_cogs`, `impairment_severance`, `other_unallocated_net`, `other_income_net`, `interest_expense`, `non_service_pension_income`, `other_non_operating_income`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Product segment revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services segment revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of sales as % of total revenue, delta vs Q-4 |
| `other_income_net_yoy` | `other_income_net` | Yıllık büyüme | Other income (operating) YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | Interest expense YoY growth rate vs Q-4 |
| `non_service_pension_income_yoy` | `non_service_pension_income` | Yıllık büyüme | non_service_pension_income YoY growth rate vs Q-4 |
| `other_non_operating_income_abs` | `other_non_operating_income` | Doğrudan tutar veya adet | other_non_operating_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## LMT_2026Q1

Geçmiş dayanak kalemleri: `products_revenue`, `services_revenue`, `products_cogs`, `services_cogs`, `other_unallocated_net`, `other_income_net`, `interest_expense`, `non_service_fas_pension_expense`, `other_non_operating_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_revenue` | Yıllık büyüme | Products sales YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services sales YoY growth rate vs Q-4 |
| `products_cogs_margin_delta_bps` | `products_cogs / çapa: products_revenue` | Marj değişimi, baz puan | Products cost as a percentage of products sales, basis-point change vs Q-4 |
| `services_cogs_margin_delta_bps` | `services_cogs / çapa: services_revenue` | Marj değişimi, baz puan | Services cost as a percentage of services sales, basis-point change vs Q-4 |
| `other_unallocated_net_yoy` | `other_unallocated_net` | Yıllık büyüme | other_unallocated_net YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `non_service_fas_pension_expense_yoy` | `non_service_fas_pension_expense` | Yıllık büyüme | non_service_fas_pension_expense YoY growth rate vs Q-4 |
| `other_non_operating_income_net_abs` | `other_non_operating_income_net` | Doğrudan tutar veya adet | other_non_operating_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## LOW_2025Q4

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_sales`, `sga`, `depreciation`, `interest_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales (revenue) YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: net_sales` | Marj değişimi, baz puan | Cost of sales as % of net sales, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | SG&A as % of net sales, delta vs Q-4 |
| `depreciation_yoy` | `depreciation` | Yıllık büyüme | Depreciation and amortization YoY growth rate vs Q-4 |
| `interest_net_yoy` | `interest_net` | Yıllık büyüme | interest_net YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## LULU_2025Q3

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_goods_sold`, `selling_general_admin`, `impairment_restructuring`, `amortization_intangible`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_goods_sold / çapa: net_revenue` | Marj değişimi, baz puan | COGS as % of net revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `selling_general_admin / çapa: net_revenue` | Marj değişimi, baz puan | SG&A as % of net revenue, delta vs Q-4 |
| `impairment_restructuring_abs` | `impairment_restructuring` | Doğrudan tutar veya adet | impairment_restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `amortization_intangible_yoy` | `amortization_intangible` | Yıllık büyüme | amortization_intangible YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## LULU_2025Q4

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_goods_sold`, `selling_general_and_administrative_expenses`, `impairment_of_goodwill_and_other_assets_restructuring_costs`, `amortization_of_intangible_assets`, `gain_on_disposal_of_assets`, `other_income_expense_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cost_of_goods_sold_margin_delta_bps` | `cost_of_goods_sold / çapa: net_revenue` | Marj değişimi, baz puan | COGS as % of net revenue, delta vs Q-4 |
| `selling_general_and_administrative_expenses_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: net_revenue` | Marj değişimi, baz puan | SG&A as % of net revenue, delta vs Q-4 |
| `other_income_expense_net_margin_delta_bps` | `other_income_expense_net / çapa: net_revenue` | Marj değişimi, baz puan | Other income (expense), net as % of net revenue, delta vs Q-4 |
| `impairment_of_goodwill_and_other_assets_restructuring_costs_abs` | `impairment_of_goodwill_and_other_assets_restructuring_costs` | Doğrudan tutar veya adet | impairment_of_goodwill_and_other_assets_restructuring_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `amortization_of_intangible_assets_yoy` | `amortization_of_intangible_assets` | Yıllık büyüme | amortization_of_intangible_assets YoY growth rate vs Q-4 |
| `gain_on_disposal_of_assets_abs` | `gain_on_disposal_of_assets` | Doğrudan tutar veya adet | gain_on_disposal_of_assets absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MA_2025Q4

Geçmiş dayanak kalemleri: `net_revenue`, `general_and_administrative`, `advertising_and_marketing`, `depreciation_and_amortization`, `provision_for_litigation`, `investment_income`, `gains_losses_on_equity_investments_net`, `interest_expense`, `other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `advertising_and_marketing_yoy` | `advertising_and_marketing` | Yıllık büyüme | Advertising and marketing expense YoY growth rate vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | Depreciation and amortization expense YoY growth rate vs Q-4 |
| `provision_for_litigation_yoy` | `provision_for_litigation` | Yıllık büyüme | Provision for litigation expense YoY growth rate vs Q-4 |
| `investment_income_abs` | `investment_income` | Doğrudan tutar veya adet | investment_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `gains_losses_on_equity_investments_net_abs` | `gains_losses_on_equity_investments_net` | Doğrudan tutar veya adet | gains_losses_on_equity_investments_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MA_2026Q1

Geçmiş dayanak kalemleri: `net_revenue`, `general_and_administrative`, `advertising_and_marketing`, `depreciation_and_amortization`, `provision_for_litigation`, `investment_income`, `losses_on_equity_investments_net`, `interest_expense`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs 2025Q1 |
| `total_opex_yoy` | `total_opex` | Yıllık büyüme | Total operating expenses YoY growth rate vs 2025Q1 |
| `total_other_income_margin_delta_bps` | `total_other_income / çapa: net_revenue` | Marj değişimi, baz puan | Total other income (expense) as a percentage of net revenue, delta vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## MCD_2025Q4

Geçmiş dayanak kalemleri: `company_owned_sales`, `franchised_revenue`, `other_revenue`, `company_owned_expenses`, `franchised_occupancy`, `other_restaurant_expenses`, `sga_depreciation`, `sga_other`, `other_operating_income_expense`, `interest_expense`, `nonoperating_income_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `company_owned_sales_yoy` | `company_owned_sales` | Yıllık büyüme | Company-owned restaurant sales YoY growth rate vs Q-4 |
| `franchised_revenue_yoy` | `franchised_revenue` | Yıllık büyüme | Franchised revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `company_owned_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Company-owned restaurant expenses as % of total revenue, delta vs Q-4 |
| `franchised_occupancy_margin_delta_bps` | `franchised_occupancy / çapa: total_revenue` | Marj değişimi, baz puan | Franchised occupancy expenses as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga_total / çapa: total_revenue` | Marj değişimi, baz puan | SG&A (depreciation and other) as % of total revenue, delta vs Q-4 |
| `other_restaurant_expenses_yoy` | `other_restaurant_expenses` | Yıllık büyüme | other_restaurant_expenses YoY growth rate vs Q-4 |
| `other_operating_income_expense_abs` | `other_operating_income_expense` | Doğrudan tutar veya adet | other_operating_income_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `nonoperating_income_expense_abs` | `nonoperating_income_expense` | Doğrudan tutar veya adet | nonoperating_income_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MELI_2025Q4

Geçmiş dayanak kalemleri: `net_service_revenues_and_financial_income`, `net_product_revenues`, `cost_of_net_revenues_and_financial_expenses`, `product_and_technology_development`, `sales_and_marketing`, `provision_for_doubtful_accounts`, `general_and_administrative`, `interest_income_and_other_financial_gains`, `interest_expense_and_other_financial_losses`, `foreign_currency_losses_net`, `equity_in_earnings_of_unconsolidated_entity`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_service_revenues_and_financial_income_yoy` | `net_service_revenues_and_financial_income` | Yıllık büyüme | Service revenues and financial income YoY growth rate vs Q-4 |
| `net_product_revenues_yoy` | `net_product_revenues` | Yıllık büyüme | Product revenues YoY growth rate vs Q-4 |
| `cost_of_net_revenues_and_financial_expenses_margin_delta_bps` | `cost_of_net_revenues_and_financial_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Cost of net revenues as percentage of total revenue, delta vs Q-4 |
| `product_and_technology_development_margin_delta_bps` | `product_and_technology_development / çapa: total_revenue` | Marj değişimi, baz puan | Product and technology development expense as percentage of total revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing expense as percentage of total revenue, delta vs Q-4 |
| `provision_for_doubtful_accounts_yoy` | `provision_for_doubtful_accounts` | Yıllık büyüme | provision_for_doubtful_accounts YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | general_and_administrative YoY growth rate vs Q-4 |
| `interest_income_and_other_financial_gains_abs` | `interest_income_and_other_financial_gains` | Doğrudan tutar veya adet | interest_income_and_other_financial_gains absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_and_other_financial_losses_abs` | `interest_expense_and_other_financial_losses` | Doğrudan tutar veya adet | interest_expense_and_other_financial_losses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `foreign_currency_losses_net_abs` | `foreign_currency_losses_net` | Doğrudan tutar veya adet | foreign_currency_losses_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_earnings_of_unconsolidated_entity_abs` | `equity_in_earnings_of_unconsolidated_entity` | Doğrudan tutar veya adet | equity_in_earnings_of_unconsolidated_entity absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MELI_2026Q1

Geçmiş dayanak kalemleri: `net_service_revenues_and_financial_income`, `net_product_revenues`, `cost_of_net_revenues_and_financial_expenses`, `product_and_technology_development`, `sales_and_marketing`, `provision_for_doubtful_accounts`, `general_and_administrative`, `interest_income_and_other_financial_gains`, `interest_expense_and_other_financial_losses`, `foreign_currency_losses_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_service_revenues_and_financial_income_yoy` | `net_service_revenues_and_financial_income` | Yıllık büyüme | Service revenues and financial income YoY growth vs Q-4 2025Q1 |
| `net_product_revenues_yoy` | `net_product_revenues` | Yıllık büyüme | Product revenues YoY growth vs Q-4 2025Q1 |
| `cost_of_revenues_margin_delta_bps` | `cost_of_net_revenues_and_financial_expenses / çapa: net_revenues` | Marj değişimi, baz puan | Cost of net revenues and financial expenses as % of net revenues, delta vs Q-4 |
| `product_and_technology_development_margin_delta_bps` | `product_and_technology_development / çapa: net_revenues` | Marj değişimi, baz puan | Product and technology development expense as % of net revenues, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: net_revenues` | Marj değişimi, baz puan | Sales and marketing expense as % of net revenues, delta vs Q-4 |
| `provision_for_doubtful_accounts_margin_delta_bps` | `provision_for_doubtful_accounts / çapa: net_revenues` | Marj değişimi, baz puan | Provision for doubtful accounts as % of net revenues, delta vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | general_and_administrative YoY growth rate vs Q-4 |
| `interest_income_and_other_financial_gains_abs` | `interest_income_and_other_financial_gains` | Doğrudan tutar veya adet | interest_income_and_other_financial_gains absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_and_other_financial_losses_abs` | `interest_expense_and_other_financial_losses` | Doğrudan tutar veya adet | interest_expense_and_other_financial_losses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `foreign_currency_losses_net_abs` | `foreign_currency_losses_net` | Doğrudan tutar veya adet | foreign_currency_losses_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## META_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `rd`, `marketing_and_sales`, `general_and_administrative`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cost_of_revenue_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `marketing_and_sales_margin_delta_bps` | `marketing_and_sales / çapa: revenue` | Marj değişimi, baz puan | Marketing and sales as % of revenue, delta vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | General and administrative as % of revenue, delta vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MRK_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `sga`, `rd`, `restructuring_costs`, `other_expense_net`, `tax_rate`, `shares`, `nci`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Sales YoY growth rate vs Q-4 2024 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as percentage of revenue, delta vs Q-4 2024 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 2024 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A as percentage of revenue, delta vs Q-4 2024 |
| `restructuring_costs_abs` | `restructuring_costs` | Doğrudan tutar veya adet | restructuring_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MRK_2026Q1

Geçmiş dayanak kalemleri: `sales`, `cost_of_sales`, `sga`, `rd`, `restructuring_costs`, `other_income_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_yoy` | `sales` | Yıllık büyüme | Sales year-over-year growth rate vs 2025Q1 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: sales` | Marj değişimi, baz puan | Cost of sales as a percentage of sales, basis point change vs Q-4 baseline |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense year-over-year growth rate vs 2025Q1 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense year-over-year growth rate vs 2025Q1 |
| `restructuring_costs_abs` | `restructuring_costs` | Doğrudan tutar veya adet | restructuring_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## MSFT_2026Q2

Geçmiş dayanak kalemleri: `product_revenue`, `service_and_other_revenue`, `product_cogs`, `service_and_other_cogs`, `research_and_development`, `sales_and_marketing`, `general_and_administrative`, `other_expense_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `service_and_other_revenue_yoy` | `service_and_other_revenue` | Yıllık büyüme | Service and other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total COGS as % of total revenue, delta vs Q-4 |
| `research_and_development_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_and_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MSFT_2026Q3

Geçmiş dayanak kalemleri: `product_revenue`, `service_and_other_revenue`, `product_cogs`, `service_and_other_cogs`, `rd`, `sales_and_marketing`, `general_and_administrative`, `other_expense_net`, `income_taxes`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `service_and_other_revenue_yoy` | `service_and_other_revenue` | Yıllık büyüme | Service and other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of revenue as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_and_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## MS_2025Q4

Geçmiş dayanak kalemleri: `investment_banking_revenue`, `trading_revenue`, `investments_revenue`, `commissions_and_fees_revenue`, `asset_management_revenue`, `other_revenue`, `interest_income`, `interest_expense`, `provision_for_credit_losses`, `compensation_and_benefits`, `brokerage_clearing_and_exchange_fees`, `information_processing_and_communications`, `professional_services`, `occupancy_and_equipment`, `marketing_and_business_development`, `other_non_interest_expense`, `net_income_noncontrolling_interests`, `preferred_stock_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `investment_banking_revenue_yoy` | `investment_banking_revenue` | Yıllık büyüme | Investment banking revenue YoY growth rate vs Q-4 |
| `trading_revenue_yoy` | `trading_revenue` | Yıllık büyüme | Trading revenue YoY growth rate vs Q-4 |
| `commissions_and_fees_revenue_yoy` | `commissions_and_fees_revenue` | Yıllık büyüme | Commissions and fees revenue YoY growth rate vs Q-4 |
| `asset_management_revenue_yoy` | `asset_management_revenue` | Yıllık büyüme | Asset management revenue YoY growth rate vs Q-4 |
| `total_non_interest_expenses_margin_delta_bps` | `total_non_interest_expenses / çapa: total_non_interest_revenues` | Marj değişimi, baz puan | Total non-interest expenses as % of non-interest revenues, delta vs Q-4 |
| `investments_revenue_abs` | `investments_revenue` | Doğrudan tutar veya adet | investments_revenue absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | other_revenue YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `provision_for_credit_losses_yoy` | `provision_for_credit_losses` | Yıllık büyüme | provision_for_credit_losses YoY growth rate vs Q-4 |
| `net_income_noncontrolling_interests_abs` | `net_income_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MU_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `cogs`, `rd`, `sga`, `other_operating_income_net`, `interest_income`, `interest_expense`, `other_non_operating_income_expense_net`, `equity_in_net_income`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cogs / çapa: revenue` | Marj değişimi, baz puan | COGS as % of revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `other_operating_income_net_abs` | `other_operating_income_net` | Doğrudan tutar veya adet | other_operating_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_non_operating_income_expense_net_abs` | `other_non_operating_income_expense_net` | Doğrudan tutar veya adet | other_non_operating_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_net_income_abs` | `equity_in_net_income` | Doğrudan tutar veya adet | equity_in_net_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MU_2026Q2

Geçmiş dayanak kalemleri: `revenue`, `cogs`, `rd`, `sga`, `other_operating_income_expense_net`, `interest_income`, `interest_expense`, `other_non_operating_income_expense_net`, `equity_in_net_income`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cogs / çapa: revenue` | Marj değişimi, baz puan | COGS as % of revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `other_operating_income_expense_net_abs` | `other_operating_income_expense_net` | Doğrudan tutar veya adet | other_operating_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_non_operating_income_expense_net_abs` | `other_non_operating_income_expense_net` | Doğrudan tutar veya adet | other_non_operating_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_net_income_abs` | `equity_in_net_income` | Doğrudan tutar veya adet | equity_in_net_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## MU_2026Q3

Geçmiş dayanak kalemleri: `revenue`, `cogs`, `rd`, `sga`, `other_operating_expense_net`, `interest_income`, `interest_expense`, `other_nonoperating_expense_net`, `equity_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cogs / çapa: revenue` | Marj değişimi, baz puan | Cost of goods sold as a percentage of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `other_operating_expense_net_abs` | `other_operating_expense_net` | Doğrudan tutar veya adet | other_operating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_nonoperating_expense_net_abs` | `other_nonoperating_expense_net` | Doğrudan tutar veya adet | other_nonoperating_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_income_net_abs` | `equity_income_net` | Doğrudan tutar veya adet | equity_income_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## M_2025Q3

Geçmiş dayanak kalemleri: `net_sales`, `other_revenue`, `cost_of_sales`, `sga`, `gains_on_sale_of_real_estate`, `impairment_restructuring_other_benefits`, `benefit_plan_income_net`, `settlement_charges`, `interest_expense_net`, `losses_on_early_retirement_of_debt`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `gains_on_sale_of_real_estate_abs` | `gains_on_sale_of_real_estate` | Doğrudan tutar veya adet | gains_on_sale_of_real_estate absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `impairment_restructuring_other_benefits_abs` | `impairment_restructuring_other_benefits` | Doğrudan tutar veya adet | impairment_restructuring_other_benefits absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `benefit_plan_income_net_yoy` | `benefit_plan_income_net` | Yıllık büyüme | benefit_plan_income_net YoY growth rate vs Q-4 |
| `settlement_charges_abs` | `settlement_charges` | Doğrudan tutar veya adet | settlement_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `losses_on_early_retirement_of_debt_abs` | `losses_on_early_retirement_of_debt` | Doğrudan tutar veya adet | losses_on_early_retirement_of_debt absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## M_2025Q4

Geçmiş dayanak kalemleri: `net_sales`, `other_revenue`, `total_revenue`, `cost_of_sales`, `selling_general_and_administrative_expenses`, `gains_on_sale_of_real_estate`, `impairment_restructuring_and_other_costs`, `benefit_plan_income_net`, `settlement_charges`, `interest_expense_net`, `losses_on_early_retirement_of_debt`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `selling_general_and_administrative_expenses / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `benefit_plan_income_net_yoy` | `benefit_plan_income_net` | Yıllık büyüme | Benefit plan income YoY growth rate vs Q-4 |
| `impairment_restructuring_and_other_costs_yoy` | `impairment_restructuring_and_other_costs` | Yıllık büyüme | Impairment, restructuring and other costs YoY growth rate vs Q-4 |
| `gains_on_sale_of_real_estate_abs` | `gains_on_sale_of_real_estate` | Doğrudan tutar veya adet | gains_on_sale_of_real_estate absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `settlement_charges_abs` | `settlement_charges` | Doğrudan tutar veya adet | settlement_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `losses_on_early_retirement_of_debt_abs` | `losses_on_early_retirement_of_debt` | Doğrudan tutar veya adet | losses_on_early_retirement_of_debt absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## NFLX_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenues`, `sales_and_marketing`, `technology_and_development`, `general_and_administrative`, `interest_expense`, `interest_and_other_income`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenues / çapa: revenue` | Marj değişimi, baz puan | Cost of revenues as % of revenue, delta vs Q-4 |
| `marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `tech_dev_yoy` | `technology_and_development` | Yıllık büyüme | Technology and development expense YoY growth rate vs Q-4 |
| `ga_margin_delta_bps` | `general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | General and administrative as % of revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_abs` | `interest_and_other_income` | Doğrudan tutar veya adet | interest_and_other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## NFLX_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenues`, `sales_marketing`, `technology_development`, `general_administrative`, `interest_expense`, `interest_and_other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cost_of_revenues_margin_delta_bps` | `cost_of_revenues / çapa: revenue` | Marj değişimi, baz puan | Cost of revenues as a percentage of revenue, delta vs Q-4 |
| `sales_marketing_margin_delta_bps` | `sales_marketing / çapa: revenue` | Marj değişimi, baz puan | Sales and marketing expense as a percentage of revenue, delta vs Q-4 |
| `technology_development_yoy` | `technology_development` | Yıllık büyüme | Technology and development expense YoY growth rate vs Q-4 |
| `general_administrative_yoy` | `general_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_and_other_income_net_abs` | `interest_and_other_income_net` | Doğrudan tutar veya adet | interest_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## NKE_2026Q2

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `demand_creation_expense`, `operating_overhead_expense`, `interest_expense_income_net`, `other_income_expense_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | Cost of sales as % of revenue, delta vs Q-4 |
| `demand_creation_expense_yoy` | `demand_creation_expense` | Yıllık büyüme | Demand creation expense YoY growth rate vs Q-4 |
| `operating_overhead_expense_yoy` | `operating_overhead_expense` | Yıllık büyüme | Operating overhead expense YoY growth rate vs Q-4 |
| `interest_expense_income_net_abs` | `interest_expense_income_net` | Doğrudan tutar veya adet | interest_expense_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## NVDA_2026Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `research_and_development`, `sales_general_and_administrative`, `acquisition_termination_cost`, `interest_income`, `interest_expense`, `other_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `rd_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sales_general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `acquisition_termination_cost_abs` | `acquisition_termination_cost` | Doğrudan tutar veya adet | acquisition_termination_cost absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_net_yoy` | `other_net` | Yıllık büyüme | other_net YoY growth rate vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## NVDA_2027Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `rd`, `sga`, `interest_income`, `interest_expense`, `other_net_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_net_expense_yoy` | `other_net_expense` | Yıllık büyüme | other_net_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## ORCL_2026Q2

Geçmiş dayanak kalemleri: `cloud_services_revenue`, `cloud_license_revenue`, `hardware_revenue`, `services_revenue`, `cloud_services_cost`, `hardware_cost`, `services_cost`, `sales_marketing`, `research_development`, `general_administrative`, `amortization_intangible`, `acquisition_related`, `restructuring`, `interest_expense`, `non_operating_income`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `cloud_revenue_yoy` | `cloud_revenue` | Yıllık büyüme | Cloud services and license support revenue YoY growth rate vs Q-4 |
| `hardware_revenue_yoy` | `hardware_revenue` | Yıllık büyüme | Hardware revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `cost_of_revenue_margin_delta_bps` | `total_cost_of_revenue / çapa: total_revenue` | Marj değişimi, baz puan | Cost of revenue as % of total revenue, delta vs Q-4 |
| `opex_margin_delta_bps` | `total_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Operating expenses as % of total revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `non_operating_income_abs` | `non_operating_income` | Doğrudan tutar veya adet | non_operating_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## ORCL_2026Q3

Geçmiş dayanak kalemleri: `cloud_services_revenue`, `cloud_license_revenue`, `hardware_revenue`, `services_revenue`, `cloud_services_cost`, `hardware_cost`, `services_cost`, `sales_marketing`, `rd`, `ga`, `amortization`, `acquisition_related`, `restructuring`, `interest_expense`, `non_operating_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `cloud_revenue_yoy` | `cloud_revenue` | Yıllık büyüme | Cloud services and license support revenue YoY growth rate vs Q-4 |
| `hardware_revenue_yoy` | `hardware_revenue` | Yıllık büyüme | Hardware revenue YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `opex_margin_delta_bps` | `total_opex / çapa: total_revenue` | Marj değişimi, baz puan | Total operating expenses as % of total revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `non_operating_expense_abs` | `non_operating_expense` | Doğrudan tutar veya adet | non_operating_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PANW_2026Q2

Geçmiş dayanak kalemleri: `product_revenue`, `subscription_support_revenue`, `product_cogs`, `subscription_support_cogs`, `rd`, `sales_marketing`, `general_administrative`, `interest_expense`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `subscription_support_revenue_yoy` | `subscription_support_revenue` | Yıllık büyüme | Subscription and support revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_marketing_margin_delta_bps` | `sales_marketing / çapa: total_revenue` | Marj değişimi, baz puan | Sales and marketing as % of total revenue, delta vs Q-4 |
| `general_administrative_margin_delta_bps` | `general_administrative / çapa: total_revenue` | Marj değişimi, baz puan | General and administrative as % of total revenue, delta vs Q-4 |
| `interest_expense_abs` | `interest_expense` | Doğrudan tutar veya adet | interest_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PANW_2026Q3

Geçmiş dayanak kalemleri: `product_revenue`, `subscription_and_support_revenue`, `product_cogs`, `subscription_and_support_cogs`, `rd`, `sales_and_marketing`, `general_and_administrative`, `interest_expense`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenue_yoy` | `product_revenue` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `subscription_and_support_revenue_yoy` | `subscription_and_support_revenue` | Yıllık büyüme | Subscription and support revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total cost of revenue as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_and_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `interest_expense_abs` | `interest_expense` | Doğrudan tutar veya adet | interest_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PEP_2026Q1

Geçmiş dayanak kalemleri: `net_revenue`, `cost_of_sales`, `sga`, `other_pension_income`, `net_interest_expense_and_other`, `tax_rate`, `shares`, `noncontrolling_interests`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: net_revenue` | Marj değişimi, baz puan | Cost of sales as % of net revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_revenue` | Marj değişimi, baz puan | SG&A as % of net revenue, delta vs Q-4 |
| `other_pension_income_yoy` | `other_pension_income` | Yıllık büyüme | other_pension_income YoY growth rate vs Q-4 |
| `net_interest_expense_and_other_yoy` | `net_interest_expense_and_other` | Yıllık büyüme | net_interest_expense_and_other YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |

## PFE_2025Q4

Geçmiş dayanak kalemleri: `product_revenues`, `alliance_revenues`, `royalty_revenues`, `cost_of_sales`, `sga`, `rd`, `acquired_ip_rd`, `amortization_intangible`, `restructuring_charges`, `other_income_net`, `discontinued_ops`, `noncontrolling_interests`, `shares`, `tax_provision`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenues_yoy` | `product_revenues` | Yıllık büyüme | Product revenues YoY growth rate vs Q-4 |
| `alliance_revenues_yoy` | `alliance_revenues` | Yıllık büyüme | Alliance revenues YoY growth rate vs Q-4 |
| `royalty_revenues_yoy` | `royalty_revenues` | Yıllık büyüme | Royalty revenues YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `acquired_ip_rd_abs` | `acquired_ip_rd` | Doğrudan tutar veya adet | acquired_ip_rd absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `amortization_intangible_yoy` | `amortization_intangible` | Yıllık büyüme | amortization_intangible YoY growth rate vs Q-4 |
| `restructuring_charges_abs` | `restructuring_charges` | Doğrudan tutar veya adet | restructuring_charges absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `discontinued_ops_abs` | `discontinued_ops` | Doğrudan tutar veya adet | discontinued_ops absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_amount` | `tax_provision` | Doğrudan tutar veya adet | Income tax provision/expense for the target quarter, in DOLLARS (same units as the Q-4 baseline) — NOT a rate. Pretax income is near zero or negative this quarter, which makes an effective tax RATE numerically meaningless (a small pretax swing produces an enormous rate swing). Predict the dollar tax provision directly; sign matters (a tax BENEFIT is negative). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## PFE_2026Q1

Geçmiş dayanak kalemleri: `product_revenues`, `alliance_revenues`, `royalty_revenues`, `cost_of_sales`, `sga`, `rd`, `acquired_iprd`, `amortization_intangible_assets`, `restructuring_acquisition_costs`, `other_income_deductions_net`, `income_taxes`, `discontinued_operations_net`, `nci`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenues_yoy` | `product_revenues` | Yıllık büyüme | Product revenue YoY growth rate vs 2025Q1 |
| `alliance_revenues_yoy` | `alliance_revenues` | Yıllık büyüme | Alliance revenue YoY growth rate vs 2025Q1 |
| `royalty_revenues_yoy` | `royalty_revenues` | Yıllık büyüme | Royalty revenue YoY growth rate vs 2025Q1 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs 2025Q1 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs 2025Q1 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | Selling, informational and administrative expenses as % of total revenue, delta vs 2025Q1 |
| `acquired_iprd_abs` | `acquired_iprd` | Doğrudan tutar veya adet | acquired_iprd absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `amortization_intangible_assets_yoy` | `amortization_intangible_assets` | Yıllık büyüme | amortization_intangible_assets YoY growth rate vs Q-4 |
| `restructuring_acquisition_costs_abs` | `restructuring_acquisition_costs` | Doğrudan tutar veya adet | restructuring_acquisition_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_deductions_net_abs` | `other_income_deductions_net` | Doğrudan tutar veya adet | other_income_deductions_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `discontinued_operations_net_abs` | `discontinued_operations_net` | Doğrudan tutar veya adet | discontinued_operations_net absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PG_2026Q2

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_products_sold`, `sga`, `intangible_impairment`, `interest_expense`, `interest_income`, `other_non_operating_income`, `net_earnings_nci`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_products_sold / çapa: net_sales` | Marj değişimi, baz puan | COGS as % of net sales, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | SG&A as % of net sales, delta vs Q-4 |
| `other_income_yoy` | `other_non_operating_income` | Yıllık büyüme | Other non-operating income YoY growth rate vs Q-4 |
| `intangible_impairment_abs` | `intangible_impairment` | Doğrudan tutar veya adet | intangible_impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `net_earnings_nci_abs` | `net_earnings_nci` | Doğrudan tutar veya adet | net_earnings_nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## PG_2026Q3

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_products_sold`, `sga`, `intangible_impairment`, `interest_expense`, `interest_income`, `other_non_operating_income_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_products_sold / çapa: total_revenue` | Marj değişimi, baz puan | Cost of products sold as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `intangible_impairment_abs` | `intangible_impairment` | Doğrudan tutar veya adet | intangible_impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `other_non_operating_income_net_abs` | `other_non_operating_income_net` | Doğrudan tutar veya adet | other_non_operating_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PLTR_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `sales_and_marketing`, `research_and_development`, `general_and_administrative`, `interest_income`, `other_income_expense_net`, `noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `rd_yoy` | `research_and_development` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: revenue` | Marj değişimi, baz puan | Sales and marketing as % of revenue, delta vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | General and administrative as % of revenue, delta vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PLUG_2025Q4

Geçmiş dayanak kalemleri: `equipment_revenue`, `services_revenue`, `ppa_revenue`, `fuel_revenue`, `other_revenue`, `equipment_cogs`, `services_cogs`, `provision_loss_contracts_cogs`, `ppa_cogs`, `fuel_cogs`, `other_cogs`, `rd`, `sga`, `restructuring`, `impairment`, `change_contingent_consideration`, `other_expense_net`, `nci_loss`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `total_revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `other_expense_margin_delta_bps` | `other_expense_net / çapa: total_revenue` | Marj değişimi, baz puan | Other expense net as % of total revenue, delta vs Q-4 |
| `provision_loss_contracts_yoy` | `provision_loss_contracts_cogs` | Yıllık büyüme | Provision for loss contracts YoY growth rate vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `impairment_abs` | `impairment` | Doğrudan tutar veya adet | impairment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `change_contingent_consideration_abs` | `change_contingent_consideration` | Doğrudan tutar veya adet | change_contingent_consideration absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `nci_loss_abs` | `nci_loss` | Doğrudan tutar veya adet | nci_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## PYPL_2025Q4

Geçmiş dayanak kalemleri: `net_revenues`, `transaction_expense`, `transaction_and_credit_losses`, `customer_support_and_operations`, `sales_and_marketing`, `technology_and_development`, `general_and_administrative`, `restructuring_and_other`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `net_revenues` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `transaction_expense_margin_delta_bps` | `transaction_expense / çapa: net_revenues` | Marj değişimi, baz puan | Transaction expense as % of net revenue, delta vs Q-4 |
| `transaction_credit_losses_margin_delta_bps` | `transaction_and_credit_losses / çapa: net_revenues` | Marj değişimi, baz puan | Transaction and credit losses as % of net revenue, delta vs Q-4 |
| `customer_support_margin_delta_bps` | `customer_support_and_operations / çapa: net_revenues` | Marj değişimi, baz puan | Customer support and operations as % of net revenue, delta vs Q-4 |
| `sales_marketing_margin_delta_bps` | `sales_and_marketing / çapa: net_revenues` | Marj değişimi, baz puan | Sales and marketing as % of net revenue, delta vs Q-4 |
| `technology_development_margin_delta_bps` | `technology_and_development / çapa: net_revenues` | Marj değişimi, baz puan | Technology and development as % of net revenue, delta vs Q-4 |
| `general_administrative_margin_delta_bps` | `general_and_administrative / çapa: net_revenues` | Marj değişimi, baz puan | General and administrative as % of net revenue, delta vs Q-4 |
| `restructuring_and_other_abs` | `restructuring_and_other` | Doğrudan tutar veya adet | restructuring_and_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## PYPL_2026Q1

Geçmiş dayanak kalemleri: `net_revenues`, `transaction_expense`, `transaction_and_credit_losses`, `customer_support_and_operations`, `sales_and_marketing`, `technology_and_development`, `general_and_administrative`, `restructuring_and_other`, `other_income_net`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenues_yoy` | `net_revenues` | Yıllık büyüme | Total net revenue YoY growth rate vs 2025Q1 |
| `transaction_expense_margin_delta_bps` | `transaction_expense / çapa: net_revenues` | Marj değişimi, baz puan | Transaction expense as a percentage of net revenues, delta bps vs 2025Q1 |
| `transaction_and_credit_losses_margin_delta_bps` | `transaction_and_credit_losses / çapa: net_revenues` | Marj değişimi, baz puan | Transaction and credit losses as a percentage of net revenues, delta bps vs 2025Q1 |
| `customer_support_and_operations_yoy` | `customer_support_and_operations` | Yıllık büyüme | Customer support and operations expense YoY growth rate vs 2025Q1 |
| `sales_and_marketing_yoy` | `sales_and_marketing` | Yıllık büyüme | Sales and marketing expense YoY growth rate vs 2025Q1 |
| `technology_and_development_yoy` | `technology_and_development` | Yıllık büyüme | Technology and development expense YoY growth rate vs 2025Q1 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | general_and_administrative YoY growth rate vs Q-4 |
| `restructuring_and_other_abs` | `restructuring_and_other` | Doğrudan tutar veya adet | restructuring_and_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## QCOM_2026Q1

Geçmiş dayanak kalemleri: `equipment_services_revenue`, `licensing_revenue`, `cost_of_revenues`, `rd`, `sga`, `other_income_expense_net`, `interest_expense`, `investment_and_other_income_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `equipment_services_revenue_yoy` | `equipment_services_revenue` | Yıllık büyüme | Equipment and services revenue YoY growth rate vs Q-4 |
| `licensing_revenue_yoy` | `licensing_revenue` | Yıllık büyüme | Licensing revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_revenues / çapa: total_revenue` | Marj değişimi, baz puan | Cost of revenues as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_and_other_income_net_abs` | `investment_and_other_income_net` | Doğrudan tutar veya adet | investment_and_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## RTX_2025Q4

Geçmiş dayanak kalemleri: `products_sales`, `services_sales`, `cost_of_sales_products`, `cost_of_sales_services`, `rd`, `sga`, `other_income_net`, `non_service_pension_income`, `interest_expense_net`, `noncontrolling_interest`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_revenue_yoy` | `products_sales` | Yıllık büyüme | Products sales YoY growth rate vs Q-4 |
| `services_revenue_yoy` | `services_sales` | Yıllık büyüme | Services sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `non_service_pension_income_yoy` | `non_service_pension_income` | Yıllık büyüme | non_service_pension_income YoY growth rate vs Q-4 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## RTX_2026Q1

Geçmiş dayanak kalemleri: `products_sales`, `services_sales`, `cost_of_sales_products`, `cost_of_sales_services`, `rd`, `sga`, `other_income_net`, `non_service_pension_income`, `interest_expense_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `products_sales_yoy` | `products_sales` | Yıllık büyüme | Products sales YoY growth vs 2025Q1 baseline |
| `services_sales_yoy` | `services_sales` | Yıllık büyüme | Services sales YoY growth vs 2025Q1 baseline |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total cost of sales as % of total revenue, delta vs 2025Q1 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth vs 2025Q1 baseline |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth vs 2025Q1 baseline |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `non_service_pension_income_yoy` | `non_service_pension_income` | Yıllık büyüme | non_service_pension_income YoY growth rate vs Q-4 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SBUX_2026Q1

Geçmiş dayanak kalemleri: `company_operated_stores_revenue`, `licensed_stores_revenue`, `other_revenue`, `product_and_distribution_costs`, `store_operating_expenses`, `other_operating_expenses`, `depreciation_and_amortization_expenses`, `general_and_administrative_expenses`, `income_from_equity_investees`, `interest_income_and_other_net`, `interest_expense`, `net_earnings_attributable_to_noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `company_operated_stores_revenue_yoy` | `company_operated_stores_revenue` | Yıllık büyüme | Company-operated stores revenue YoY growth rate vs Q-4 |
| `licensed_stores_revenue_yoy` | `licensed_stores_revenue` | Yıllık büyüme | Licensed stores revenue YoY growth rate vs Q-4 |
| `product_and_distribution_costs_margin_delta_bps` | `product_and_distribution_costs / çapa: total_revenue` | Marj değişimi, baz puan | Product and distribution costs as % of total revenue, delta vs Q-4 |
| `store_operating_expenses_margin_delta_bps` | `store_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Store operating expenses as % of total revenue, delta vs Q-4 |
| `depreciation_and_amortization_expenses_margin_delta_bps` | `depreciation_and_amortization_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Depreciation and amortization expenses as % of total revenue, delta vs Q-4 |
| `general_and_administrative_expenses_margin_delta_bps` | `general_and_administrative_expenses / çapa: total_revenue` | Marj değişimi, baz puan | G&A expenses as % of total revenue, delta vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | other_revenue YoY growth rate vs Q-4 |
| `other_operating_expenses_abs` | `other_operating_expenses` | Doğrudan tutar veya adet | other_operating_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_from_equity_investees_abs` | `income_from_equity_investees` | Doğrudan tutar veya adet | income_from_equity_investees absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_and_other_net_yoy` | `interest_income_and_other_net` | Yıllık büyüme | interest_income_and_other_net YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `net_earnings_attributable_to_noncontrolling_interests_abs` | `net_earnings_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_earnings_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SBUX_2026Q2

Geçmiş dayanak kalemleri: `company_operated_stores`, `licensed_stores`, `other_revenue`, `product_and_distribution_costs`, `store_operating_expenses`, `other_operating_expenses`, `depreciation_and_amortization_expenses`, `general_and_administrative_expenses`, `restructuring`, `income_from_equity_investees`, `interest_income_and_other_net`, `interest_expense`, `noncontrolling_interest`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `company_operated_stores_yoy` | `company_operated_stores` | Yıllık büyüme | Company-operated store revenue YoY growth vs Q-4 |
| `licensed_stores_yoy` | `licensed_stores` | Yıllık büyüme | Licensed store revenue YoY growth vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth vs Q-4 |
| `product_and_distribution_costs_margin_delta_bps` | `product_and_distribution_costs / çapa: total_net_revenues` | Marj değişimi, baz puan | Product and distribution costs as % of total net revenues, delta vs Q-4 |
| `store_operating_expenses_margin_delta_bps` | `store_operating_expenses / çapa: total_net_revenues` | Marj değişimi, baz puan | Store operating expenses as % of total net revenues, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_net_revenues` | Marj değişimi, baz puan | SG&A (other operating plus G&A) as % of total net revenues, delta vs Q-4 |
| `depreciation_and_amortization_expenses_yoy` | `depreciation_and_amortization_expenses` | Yıllık büyüme | depreciation_and_amortization_expenses YoY growth rate vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_from_equity_investees_abs` | `income_from_equity_investees` | Doğrudan tutar veya adet | income_from_equity_investees absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_and_other_net_yoy` | `interest_income_and_other_net` | Yıllık büyüme | interest_income_and_other_net YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SLB_2025Q4

Geçmiş dayanak kalemleri: `services_revenue`, `product_sales`, `interest_other_income_net`, `cost_of_services`, `cost_of_sales`, `research_engineering`, `general_administrative`, `restructuring_other`, `merger_integration`, `interest_expense`, `net_income_attributable_to_noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `product_sales_yoy` | `product_sales` | Yıllık büyüme | Product sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Total COGS as % of total revenue, delta vs Q-4 |
| `research_engineering_yoy` | `research_engineering` | Yıllık büyüme | Research & engineering expense YoY growth rate vs Q-4 |
| `general_administrative_margin_delta_bps` | `general_administrative / çapa: total_revenue` | Marj değişimi, baz puan | General & administrative expense as % of total revenue, delta vs Q-4 |
| `interest_other_income_net_abs` | `interest_other_income_net` | Doğrudan tutar veya adet | interest_other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `restructuring_other_abs` | `restructuring_other` | Doğrudan tutar veya adet | restructuring_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `merger_integration_abs` | `merger_integration` | Doğrudan tutar veya adet | merger_integration absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SLB_2026Q1

Geçmiş dayanak kalemleri: `services_revenue`, `product_sales_revenue`, `interest_and_other_income`, `cost_of_services`, `cost_of_sales`, `research_and_engineering`, `general_and_administrative`, `restructuring`, `merger_and_integration`, `interest_expense`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `services_revenue_yoy` | `services_revenue` | Yıllık büyüme | Services revenue YoY growth rate vs Q-4 |
| `product_sales_revenue_yoy` | `product_sales_revenue` | Yıllık büyüme | Product sales revenue YoY growth rate vs Q-4 |
| `cost_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined cost of services and cost of sales as a percentage of total revenue, delta vs Q-4 |
| `research_and_engineering_yoy` | `research_and_engineering` | Yıllık büyüme | Research and engineering expense YoY growth rate vs Q-4 |
| `general_and_administrative_yoy` | `general_and_administrative` | Yıllık büyüme | General and administrative expense YoY growth rate vs Q-4 |
| `interest_and_other_income_abs` | `interest_and_other_income` | Doğrudan tutar veya adet | interest_and_other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `merger_and_integration_abs` | `merger_and_integration` | Doğrudan tutar veya adet | merger_and_integration absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SMCI_2026Q3

Geçmiş dayanak kalemleri: `net_sales`, `cost_of_sales`, `rd`, `sales_marketing`, `general_administrative`, `other_expense_income_net`, `interest_expense`, `tax_rate`, `equity_investee_loss`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: net_sales` | Marj değişimi, baz puan | Cost of sales as a percentage of net sales, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: net_sales` | Marj değişimi, baz puan | Combined sales & marketing and G&A as a percentage of net sales, delta vs Q-4 |
| `other_expense_income_net_abs` | `other_expense_income_net` | Doğrudan tutar veya adet | other_expense_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `equity_investee_loss_abs` | `equity_investee_loss` | Doğrudan tutar veya adet | equity_investee_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SPGI_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `operating_related_expenses`, `selling_and_general_expenses`, `depreciation`, `amortization_of_intangibles`, `gain_on_dispositions_net`, `equity_in_income_on_unconsolidated_subsidiaries`, `other_income_expense_net`, `interest_expense_net`, `loss_on_extinguishment_of_debt`, `tax_rate`, `shares`, `net_income_attributable_to_noncontrolling_interests`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `operating_related_expenses_margin_delta_bps` | `operating_related_expenses / çapa: revenue` | Marj değişimi, baz puan | Operating-related expenses as % of revenue, delta vs Q-4 |
| `selling_and_general_expenses_margin_delta_bps` | `selling_and_general_expenses / çapa: revenue` | Marj değişimi, baz puan | Selling and general expenses as % of revenue, delta vs Q-4 |
| `depreciation_margin_delta_bps` | `depreciation / çapa: revenue` | Marj değişimi, baz puan | Depreciation as % of revenue, delta vs Q-4 |
| `amortization_of_intangibles_margin_delta_bps` | `amortization_of_intangibles / çapa: revenue` | Marj değişimi, baz puan | Amortization of intangibles as % of revenue, delta vs Q-4 |
| `interest_expense_net_margin_delta_bps` | `interest_expense_net / çapa: revenue` | Marj değişimi, baz puan | Interest expense net as % of revenue, delta vs Q-4 |
| `gain_on_dispositions_net_abs` | `gain_on_dispositions_net` | Doğrudan tutar veya adet | gain_on_dispositions_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_income_on_unconsolidated_subsidiaries_abs` | `equity_in_income_on_unconsolidated_subsidiaries` | Doğrudan tutar veya adet | equity_in_income_on_unconsolidated_subsidiaries absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_expense_net_abs` | `other_income_expense_net` | Doğrudan tutar veya adet | other_income_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_on_extinguishment_of_debt_abs` | `loss_on_extinguishment_of_debt` | Doğrudan tutar veya adet | loss_on_extinguishment_of_debt absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## SPGI_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `operating_related_expenses`, `selling_and_general_expenses`, `depreciation`, `amortization_of_intangibles`, `equity_income`, `other_expense_net`, `interest_expense_net`, `tax_rate`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 baseline |
| `operating_related_expenses_margin_delta_bps` | `operating_related_expenses / çapa: revenue` | Marj değişimi, baz puan | Operating-related expenses as % of total revenue, delta vs Q-4 |
| `selling_and_general_expenses_margin_delta_bps` | `selling_and_general_expenses / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `depreciation_and_amortization_margin_delta_bps` | `depreciation_and_amortization / çapa: revenue` | Marj değişimi, baz puan | Depreciation and amortization as % of total revenue, delta vs Q-4 |
| `equity_income_abs` | `equity_income` | Doğrudan tutar veya adet | equity_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## TGT_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_sales`, `sga`, `depreciation`, `net_interest_expense`, `net_other_income`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `cost_of_sales / çapa: revenue` | Marj değişimi, baz puan | COGS as % of revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: revenue` | Marj değişimi, baz puan | SG&A as % of revenue, delta vs Q-4 |
| `depreciation_yoy` | `depreciation` | Yıllık büyüme | depreciation YoY growth rate vs Q-4 |
| `net_interest_expense_yoy` | `net_interest_expense` | Yıllık büyüme | net_interest_expense YoY growth rate vs Q-4 |
| `net_other_income_abs` | `net_other_income` | Doğrudan tutar veya adet | net_other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## TMO_2025Q4

Geçmiş dayanak kalemleri: `product_revenues`, `service_revenues`, `cost_product_revenues`, `cost_service_revenues`, `sga`, `rd`, `restructuring_and_other_costs`, `interest_income`, `interest_expense`, `other_income_net`, `equity_in_earnings_of_unconsolidated_entities`, `net_income_attributable_to_noncontrolling_interests`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenues_yoy` | `product_revenues` | Yıllık büyüme | Product revenues YoY growth rate vs Q-4 |
| `service_revenues_yoy` | `service_revenues` | Yıllık büyüme | Service revenues YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | COGS as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `restructuring_and_other_costs_yoy` | `restructuring_and_other_costs` | Yıllık büyüme | Restructuring and other costs YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `equity_in_earnings_of_unconsolidated_entities_abs` | `equity_in_earnings_of_unconsolidated_entities` | Doğrudan tutar veya adet | equity_in_earnings_of_unconsolidated_entities absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## TMO_2026Q1

Geçmiş dayanak kalemleri: `product_revenues`, `service_revenues`, `cost_of_product_revenues`, `cost_of_service_revenues`, `sga`, `rd`, `restructuring_and_other_costs`, `interest_income`, `interest_expense`, `other_income_net`, `tax_rate`, `equity_losses`, `nci`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `product_revenues_yoy` | `product_revenues` | Yıllık büyüme | Product revenue YoY growth rate vs Q-4 |
| `service_revenues_yoy` | `service_revenues` | Yıllık büyüme | Service revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined product and service COGS as % of total revenue, delta vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | SG&A expense YoY growth rate vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `restructuring_and_other_costs_abs` | `restructuring_and_other_costs` | Doğrudan tutar veya adet | restructuring_and_other_costs absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `equity_losses_abs` | `equity_losses` | Doğrudan tutar veya adet | equity_losses absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## TSLA_2025Q4

Geçmiş dayanak kalemleri: `automotive_sales`, `automotive_regulatory_credits`, `automotive_leasing`, `energy_generation_and_storage`, `services_and_other`, `automotive_sales_cogs`, `automotive_leasing_cogs`, `energy_generation_and_storage_cogs`, `services_and_other_cogs`, `research_and_development`, `selling_general_and_administrative`, `restructuring_and_other`, `interest_income`, `interest_expense`, `other_income_net`, `net_income_attributable_to_noncontrolling_interests`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `automotive_revenue_yoy` | `total_automotive_revenue` | Yıllık büyüme | Automotive revenue YoY growth rate vs Q-4 |
| `energy_generation_and_storage_yoy` | `energy_generation_and_storage` | Yıllık büyüme | Energy generation and storage revenue YoY growth rate vs Q-4 |
| `services_and_other_yoy` | `services_and_other` | Yıllık büyüme | Services and other revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenue` | Marj değişimi, baz puan | Combined COGS as % of total revenue, delta vs Q-4 |
| `opex_margin_delta_bps` | `total_opex / çapa: total_revenue` | Marj değişimi, baz puan | Operating expenses as % of total revenue, delta vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `net_income_attributable_to_noncontrolling_interests_abs` | `net_income_attributable_to_noncontrolling_interests` | Doğrudan tutar veya adet | net_income_attributable_to_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## TSLA_2026Q1

Geçmiş dayanak kalemleri: `automotive_sales_revenue`, `automotive_regulatory_credits`, `automotive_leasing_revenue`, `energy_generation_storage_revenue`, `services_and_other_revenue`, `automotive_sales_cogs`, `automotive_leasing_cogs`, `energy_generation_storage_cogs`, `services_and_other_cogs`, `rd`, `sga`, `restructuring_and_other`, `interest_income`, `interest_expense`, `other_expense_net`, `net_income_attributable_to_nci`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `automotive_sales_revenue_yoy` | `automotive_sales_revenue` | Yıllık büyüme | Automotive sales revenue YoY growth vs Q-4 |
| `automotive_regulatory_credits_yoy` | `automotive_regulatory_credits` | Yıllık büyüme | Automotive regulatory credits revenue YoY growth vs Q-4 |
| `automotive_leasing_revenue_yoy` | `automotive_leasing_revenue` | Yıllık büyüme | Automotive leasing revenue YoY growth vs Q-4 |
| `energy_generation_storage_revenue_yoy` | `energy_generation_storage_revenue` | Yıllık büyüme | Energy generation and storage revenue YoY growth vs Q-4 |
| `services_and_other_revenue_yoy` | `services_and_other_revenue` | Yıllık büyüme | Services and other revenue YoY growth vs Q-4 |
| `cogs_margin_delta_bps` | `total_cogs / çapa: total_revenues` | Marj değişimi, baz puan | Total cost of revenues as % of total revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | rd YoY growth rate vs Q-4 |
| `sga_yoy` | `sga` | Yıllık büyüme | sga YoY growth rate vs Q-4 |
| `restructuring_and_other_abs` | `restructuring_and_other` | Doğrudan tutar veya adet | restructuring_and_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_expense_net_abs` | `other_expense_net` | Doğrudan tutar veya adet | other_expense_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `net_income_attributable_to_nci_abs` | `net_income_attributable_to_nci` | Doğrudan tutar veya adet | net_income_attributable_to_nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## UAL_2025Q4

Geçmiş dayanak kalemleri: `passenger_revenue`, `cargo_revenue`, `other_operating_revenue`, `salaries_and_related_costs`, `aircraft_fuel`, `landing_fees_and_other_rent`, `aircraft_maintenance_materials_and_outside_repairs`, `depreciation_and_amortization`, `regional_capacity_purchase`, `distribution_expenses`, `aircraft_rent`, `special_charges`, `other_operating_expenses`, `interest_expense`, `interest_income`, `interest_capitalized`, `unrealized_gains_losses_on_investments_net`, `miscellaneous_net`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_revenue_yoy` | `passenger_revenue` | Yıllık büyüme | Passenger revenue YoY growth rate vs Q-4 |
| `cargo_revenue_yoy` | `cargo_revenue` | Yıllık büyüme | Cargo revenue YoY growth rate vs Q-4 |
| `other_operating_revenue_yoy` | `other_operating_revenue` | Yıllık büyüme | Other operating revenue YoY growth rate vs Q-4 |
| `op_expense_margin_delta_bps` | `total_operating_expense / çapa: total_revenue` | Marj değişimi, baz puan | Operating expenses as % of total revenue, delta vs Q-4 |
| `nonop_expense_margin_delta_bps` | `total_nonoperating_expense_net / çapa: total_revenue` | Marj değişimi, baz puan | Net nonoperating expense as % of total revenue, delta vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## UAL_2026Q1

Geçmiş dayanak kalemleri: `passenger_revenue`, `cargo_revenue`, `other_operating_revenue`, `salaries_and_related_costs`, `aircraft_fuel`, `landing_fees_and_other_rent`, `aircraft_maintenance_materials_and_outside_repairs`, `depreciation_and_amortization`, `regional_capacity_purchase`, `distribution_expenses`, `aircraft_rent`, `special_charges_credits`, `other_operating_expenses`, `interest_expense`, `interest_income`, `interest_capitalized`, `unrealized_losses_on_investments_net`, `miscellaneous_net`, `income_taxes`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `passenger_revenue_yoy` | `passenger_revenue` | Yıllık büyüme | Passenger revenue YoY growth rate vs 2025Q1 |
| `cargo_revenue_yoy` | `cargo_revenue` | Yıllık büyüme | Cargo revenue YoY growth rate vs 2025Q1 |
| `other_operating_revenue_yoy` | `other_operating_revenue` | Yıllık büyüme | Other operating revenue YoY growth rate vs 2025Q1 |
| `fuel_margin_delta_bps` | `aircraft_fuel / çapa: total_revenue` | Marj değişimi, baz puan | Aircraft fuel expense as a percentage of total revenue, delta vs 2025Q1 |
| `nonfuel_opex_margin_delta_bps` | `nonfuel_operating_expense / çapa: total_revenue` | Marj değişimi, baz puan | Non-fuel operating expenses as a percentage of total revenue, delta vs 2025Q1 |
| `special_charges_credits_abs` | `special_charges_credits` | Doğrudan tutar veya adet | special_charges_credits absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `interest_income_yoy` | `interest_income` | Yıllık büyüme | interest_income YoY growth rate vs Q-4 |
| `interest_capitalized_yoy` | `interest_capitalized` | Yıllık büyüme | interest_capitalized YoY growth rate vs Q-4 |
| `unrealized_losses_on_investments_net_abs` | `unrealized_losses_on_investments_net` | Doğrudan tutar veya adet | unrealized_losses_on_investments_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `miscellaneous_net_yoy` | `miscellaneous_net` | Yıllık büyüme | miscellaneous_net YoY growth rate vs Q-4 |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## UBER_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `operations_and_support`, `sales_and_marketing`, `research_and_development`, `general_and_administrative`, `depreciation_and_amortization`, `interest_expense`, `other_income_net`, `income_loss_equity_method_investments`, `noncontrolling_interest`, `shares`, `tax_provision`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `cost_of_revenue_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `operations_and_support_margin_delta_bps` | `operations_and_support / çapa: revenue` | Marj değişimi, baz puan | Operations and support as % of revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: revenue` | Marj değişimi, baz puan | Sales and marketing as % of revenue, delta vs Q-4 |
| `research_and_development_margin_delta_bps` | `research_and_development / çapa: revenue` | Marj değişimi, baz puan | R&D as % of revenue, delta vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | G&A as % of revenue, delta vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_loss_equity_method_investments_abs` | `income_loss_equity_method_investments` | Doğrudan tutar veya adet | income_loss_equity_method_investments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_amount` | `tax_provision` | Doğrudan tutar veya adet | Income tax provision/expense for the target quarter, in DOLLARS (same units as the Q-4 baseline) — NOT a rate. Pretax income is near zero or negative this quarter, which makes an effective tax RATE numerically meaningless (a small pretax swing produces an enormous rate swing). Predict the dollar tax provision directly; sign matters (a tax BENEFIT is negative). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## UBER_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `cost_of_revenue`, `operations_and_support`, `sales_and_marketing`, `rd`, `general_and_administrative`, `depreciation_and_amortization`, `interest_expense`, `other_income_net`, `loss_from_equity_method_investments`, `nci_net_loss`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 baseline |
| `cost_of_revenue_margin_delta_bps` | `cost_of_revenue / çapa: revenue` | Marj değişimi, baz puan | Cost of revenue as % of revenue, delta vs Q-4 |
| `operations_and_support_margin_delta_bps` | `operations_and_support / çapa: revenue` | Marj değişimi, baz puan | Operations and support as % of revenue, delta vs Q-4 |
| `sales_and_marketing_margin_delta_bps` | `sales_and_marketing / çapa: revenue` | Marj değişimi, baz puan | Sales and marketing as % of revenue, delta vs Q-4 |
| `rd_yoy` | `rd` | Yıllık büyüme | R&D expense YoY growth rate vs Q-4 |
| `general_and_administrative_margin_delta_bps` | `general_and_administrative / çapa: revenue` | Marj değişimi, baz puan | G&A as % of revenue, delta vs Q-4 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | depreciation_and_amortization YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_from_equity_method_investments_abs` | `loss_from_equity_method_investments` | Doğrudan tutar veya adet | loss_from_equity_method_investments absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `nci_net_loss_abs` | `nci_net_loss` | Doğrudan tutar veya adet | nci_net_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## UNH_2026Q1

Geçmiş dayanak kalemleri: `premiums`, `products`, `services`, `investment_other_income`, `medical_costs`, `other_operating_costs`, `cost_of_products_sold`, `depreciation_amortization`, `interest_expense`, `loss_on_sale_subsidiary`, `tax_rate`, `noncontrolling_interests`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `premiums_yoy` | `premiums` | Yıllık büyüme | Premiums revenue YoY growth rate vs 2025Q1 |
| `products_yoy` | `products` | Yıllık büyüme | Products revenue YoY growth rate vs 2025Q1 |
| `services_yoy` | `services` | Yıllık büyüme | Services revenue YoY growth rate vs 2025Q1 |
| `medical_cost_ratio_delta_bps` | `medical_costs / çapa: premiums` | Marj değişimi, baz puan | Medical costs as % of premiums, delta vs 2025Q1 |
| `products_cogs_margin_delta_bps` | `cost_of_products_sold / çapa: products` | Marj değişimi, baz puan | Cost of products sold as % of products revenue, delta vs 2025Q1 |
| `opex_margin_delta_bps` | `non_medical_opex / çapa: total_revenue` | Marj değişimi, baz puan | Operating costs excluding medical costs and product COGS as % of total revenue, delta vs 2025Q1 |
| `investment_other_income_abs` | `investment_other_income` | Doğrudan tutar veya adet | investment_other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `loss_on_sale_subsidiary_yoy` | `loss_on_sale_subsidiary` | Yıllık büyüme | loss_on_sale_subsidiary YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## UNP_2025Q4

Geçmiş dayanak kalemleri: `freight_revenues`, `other_revenues`, `compensation_and_benefits`, `purchased_services_and_materials`, `fuel`, `depreciation`, `equipment_and_other_rents`, `other_operating_expenses`, `other_income_net`, `interest_expense`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `freight_revenues_yoy` | `freight_revenues` | Yıllık büyüme | Freight revenues YoY growth rate vs Q-4 |
| `other_revenues_yoy` | `other_revenues` | Yıllık büyüme | Other revenues YoY growth rate vs Q-4 |
| `opex_margin_delta_bps` | `total_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Operating expenses as % of total revenue, delta vs Q-4 |
| `other_income_margin_delta_bps` | `other_income_net / çapa: total_revenue` | Marj değişimi, baz puan | Other income net as % of total revenue, delta vs Q-4 |
| `interest_margin_delta_bps` | `interest_expense / çapa: total_revenue` | Marj değişimi, baz puan | Interest expense as % of total revenue, delta vs Q-4 |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## UNP_2026Q1

Geçmiş dayanak kalemleri: `freight_revenue`, `other_revenue`, `compensation_and_benefits`, `purchased_services_and_materials`, `depreciation`, `fuel`, `equipment_and_other_rents`, `other_operating_expense`, `other_income_net`, `interest_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `freight_revenue_yoy` | `freight_revenue` | Yıllık büyüme | Freight revenue YoY growth rate vs Q-4 baseline |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 baseline |
| `operating_expense_margin_delta_bps` | `total_operating_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Total operating expenses as a percentage of total revenue, delta vs Q-4 baseline |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## UPS_2025Q4

Geçmiş dayanak kalemleri: `revenue`, `compensation_and_benefits`, `repairs_and_maintenance`, `depreciation_and_amortization`, `purchased_transportation`, `fuel`, `other_occupancy`, `other_expenses`, `other_income_expense`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q4-2024 |
| `compensation_and_benefits_margin_delta_bps` | `compensation_and_benefits / çapa: revenue` | Marj değişimi, baz puan | Compensation and benefits as % of revenue, delta vs Q4-2024 |
| `purchased_transportation_margin_delta_bps` | `purchased_transportation / çapa: revenue` | Marj değişimi, baz puan | Purchased transportation as % of revenue, delta vs Q4-2024 |
| `fuel_margin_delta_bps` | `fuel / çapa: revenue` | Marj değişimi, baz puan | Fuel expense as % of revenue, delta vs Q4-2024 |
| `depreciation_and_amortization_yoy` | `depreciation_and_amortization` | Yıllık büyüme | Depreciation and amortization expense YoY growth rate vs Q4-2024 |
| `repairs_and_maintenance_yoy` | `repairs_and_maintenance` | Yıllık büyüme | repairs_and_maintenance YoY growth rate vs Q-4 |
| `other_occupancy_yoy` | `other_occupancy` | Yıllık büyüme | other_occupancy YoY growth rate vs Q-4 |
| `other_expenses_abs` | `other_expenses` | Doğrudan tutar veya adet | other_expenses absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_expense_abs` | `other_income_expense` | Doğrudan tutar veya adet | other_income_expense absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## UPS_2026Q1

Geçmiş dayanak kalemleri: `revenue`, `compensation_and_benefits`, `repairs_and_maintenance`, `depreciation_and_amortization`, `purchased_transportation`, `fuel`, `other_occupancy`, `other_expenses`, `investment_income_and_other`, `interest_expense`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `compensation_and_benefits_yoy` | `compensation_and_benefits` | Yıllık büyüme | Compensation and benefits expense YoY growth rate vs Q-4 |
| `purchased_transportation_margin_delta_bps` | `purchased_transportation / çapa: revenue` | Marj değişimi, baz puan | Purchased transportation as % of revenue, delta vs Q-4 |
| `fuel_margin_delta_bps` | `fuel / çapa: revenue` | Marj değişimi, baz puan | Fuel expense as % of revenue, delta vs Q-4 |
| `other_opex_margin_delta_bps` | `other_opex_total / çapa: revenue` | Marj değişimi, baz puan | Total other operating expenses as % of revenue, delta vs Q-4 |
| `investment_income_and_other_abs` | `investment_income_and_other` | Doğrudan tutar veya adet | investment_income_and_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## V_2026Q1

Geçmiş dayanak kalemleri: `net_revenue`, `personnel`, `marketing`, `network_and_processing`, `professional_fees`, `depreciation_and_amortization`, `general_and_administrative`, `litigation_provision`, `interest_expense`, `investment_income_other`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Net revenue YoY growth rate vs Q-4 |
| `opex_margin_delta_bps` | `total_opex / çapa: net_revenue` | Marj değişimi, baz puan | Total operating expenses as % of net revenue, delta vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_income_other_abs` | `investment_income_other` | Doğrudan tutar veya adet | investment_income_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## V_2026Q2

Geçmiş dayanak kalemleri: `net_revenue`, `personnel`, `marketing`, `network_and_processing`, `professional_fees`, `depreciation_and_amortization`, `general_and_administrative`, `litigation_provision`, `interest_expense`, `investment_income_other`, `tax_rate`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_revenue_yoy` | `net_revenue` | Yıllık büyüme | Total net revenue YoY growth rate vs 2025Q2 |
| `personnel_yoy` | `personnel` | Yıllık büyüme | Personnel expense YoY growth rate vs 2025Q2 |
| `other_opex_margin_delta_bps` | `other_opex / çapa: net_revenue` | Marj değişimi, baz puan | Other operating expenses as % of net revenue, delta vs 2025Q2 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `investment_income_other_abs` | `investment_income_other` | Doğrudan tutar veya adet | investment_income_other absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## WBD_2025Q4

Geçmiş dayanak kalemleri: `distribution_revenue`, `advertising_revenue`, `content_revenue`, `other_revenue`, `cost_of_revenues`, `sga`, `depreciation`, `restructuring`, `impairments`, `interest_expense_net`, `gain_on_extinguishment`, `loss_from_equity_investees`, `other_income_net`, `noncontrolling_interests`, `redeemable_noncontrolling_interests`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `distribution_revenue_yoy` | `distribution_revenue` | Yıllık büyüme | Distribution revenue YoY growth rate vs Q-4 |
| `advertising_revenue_yoy` | `advertising_revenue` | Yıllık büyüme | Advertising revenue YoY growth rate vs Q-4 |
| `content_revenue_yoy` | `content_revenue` | Yıllık büyüme | Content revenue YoY growth rate vs Q-4 |
| `other_revenue_yoy` | `other_revenue` | Yıllık büyüme | Other revenue YoY growth rate vs Q-4 |
| `cost_of_revenues_margin_delta_bps` | `cost_of_revenues / çapa: total_revenue` | Marj değişimi, baz puan | Cost of revenues as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `depreciation_margin_delta_bps` | `depreciation / çapa: total_revenue` | Marj değişimi, baz puan | Depreciation and amortization as % of total revenue, delta vs Q-4 |
| `restructuring_abs` | `restructuring` | Doğrudan tutar veya adet | restructuring absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `impairments_abs` | `impairments` | Doğrudan tutar veya adet | impairments absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `gain_on_extinguishment_abs` | `gain_on_extinguishment` | Doğrudan tutar veya adet | gain_on_extinguishment absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_from_equity_investees_abs` | `loss_from_equity_investees` | Doğrudan tutar veya adet | loss_from_equity_investees absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `redeemable_noncontrolling_interests_abs` | `redeemable_noncontrolling_interests` | Doğrudan tutar veya adet | redeemable_noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## WBD_2026Q1

Geçmiş dayanak kalemleri: `distribution_revenue`, `advertising_revenue`, `content_revenue`, `other_revenue`, `cost_of_revenues`, `sga`, `depreciation_and_amortization`, `restructuring_and_other_charges`, `impairments_and_loss_on_dispositions`, `interest_expense_net`, `loss_on_extinguishment_of_debt`, `loss_from_equity_investees_net`, `other_income_net`, `income_taxes`, `nci`, `rnci_loss`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `total_revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 (2025Q1) |
| `cost_of_revenues_margin_delta_bps` | `cost_of_revenues / çapa: total_revenue` | Marj değişimi, baz puan | Cost of revenues as % of total revenue, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenue` | Marj değişimi, baz puan | SG&A as % of total revenue, delta vs Q-4 |
| `d_and_a_margin_delta_bps` | `depreciation_and_amortization / çapa: total_revenue` | Marj değişimi, baz puan | Depreciation and amortization as % of total revenue, delta vs Q-4 |
| `other_charges_yoy` | `other_charges` | Yıllık büyüme | Combined restructuring and impairment charges YoY growth rate vs Q-4 |
| `interest_expense_net_yoy` | `interest_expense_net` | Yıllık büyüme | interest_expense_net YoY growth rate vs Q-4 |
| `loss_on_extinguishment_of_debt_abs` | `loss_on_extinguishment_of_debt` | Doğrudan tutar veya adet | loss_on_extinguishment_of_debt absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `loss_from_equity_investees_net_abs` | `loss_from_equity_investees_net` | Doğrudan tutar veya adet | loss_from_equity_investees_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `other_income_net_abs` | `other_income_net` | Doğrudan tutar veya adet | other_income_net absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `rnci_loss_abs` | `rnci_loss` | Doğrudan tutar veya adet | rnci_loss absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## WFC_2025Q4

Geçmiş dayanak kalemleri: `debt_securities_interest_income`, `loans_held_for_sale_interest_income`, `loans_interest_income`, `equity_securities_interest_income`, `other_interest_income`, `total_interest_income`, `deposits_interest_expense`, `short_term_borrowings_interest_expense`, `long_term_debt_interest_expense`, `other_interest_expense`, `total_interest_expense`, `net_interest_income`, `deposit_and_lending_related_fees`, `investment_advisory_and_other_asset_based_fees`, `commissions_and_brokerage_services_fees`, `investment_banking_fees`, `card_fees`, `mortgage_banking`, `net_gains_from_trading_and_securities`, `other_noninterest_income`, `total_noninterest_income`, `total_revenue`, `provision_for_credit_losses`, `personnel`, `technology_telecommunications_and_equipment`, `occupancy`, `operating_losses`, `professional_and_outside_services`, `advertising_and_promotion`, `other_noninterest_expense`, `total_noninterest_expense`, `pretax_income`, `net_income_before_nci`, `net_income_nci`, `preferred_stock_dividends`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `total_revenue_yoy` | `total_revenue` | Yıllık büyüme | Total revenue YoY growth rate vs Q-4 |
| `provision_for_credit_losses_yoy` | `provision_for_credit_losses` | Yıllık büyüme | Provision for credit losses YoY growth rate vs Q-4 |
| `total_noninterest_expense_margin_delta_bps` | `total_noninterest_expense / çapa: total_revenue` | Marj değişimi, baz puan | Total noninterest expense as % of total revenue, delta vs Q-4 |
| `net_interest_income_abs` | `net_interest_income` | Doğrudan tutar veya adet | net_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `total_noninterest_income_abs` | `total_noninterest_income` | Doğrudan tutar veya adet | total_noninterest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `personnel_abs` | `personnel` | Doğrudan tutar veya adet | personnel absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `debt_securities_interest_income_abs` | `debt_securities_interest_income` | Doğrudan tutar veya adet | debt_securities_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `loans_held_for_sale_interest_income_abs` | `loans_held_for_sale_interest_income` | Doğrudan tutar veya adet | loans_held_for_sale_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `loans_interest_income_abs` | `loans_interest_income` | Doğrudan tutar veya adet | loans_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `equity_securities_interest_income_abs` | `equity_securities_interest_income` | Doğrudan tutar veya adet | equity_securities_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `other_interest_income_abs` | `other_interest_income` | Doğrudan tutar veya adet | other_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `total_interest_income_abs` | `total_interest_income` | Doğrudan tutar veya adet | total_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `deposits_interest_expense_abs` | `deposits_interest_expense` | Doğrudan tutar veya adet | deposits_interest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `short_term_borrowings_interest_expense_abs` | `short_term_borrowings_interest_expense` | Doğrudan tutar veya adet | short_term_borrowings_interest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `long_term_debt_interest_expense_abs` | `long_term_debt_interest_expense` | Doğrudan tutar veya adet | long_term_debt_interest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `other_interest_expense_abs` | `other_interest_expense` | Doğrudan tutar veya adet | other_interest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `total_interest_expense_abs` | `total_interest_expense` | Doğrudan tutar veya adet | total_interest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `deposit_and_lending_related_fees_abs` | `deposit_and_lending_related_fees` | Doğrudan tutar veya adet | deposit_and_lending_related_fees absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `investment_advisory_and_other_asset_based_fees_abs` | `investment_advisory_and_other_asset_based_fees` | Doğrudan tutar veya adet | investment_advisory_and_other_asset_based_fees absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `commissions_and_brokerage_services_fees_abs` | `commissions_and_brokerage_services_fees` | Doğrudan tutar veya adet | commissions_and_brokerage_services_fees absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `investment_banking_fees_abs` | `investment_banking_fees` | Doğrudan tutar veya adet | investment_banking_fees absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `card_fees_abs` | `card_fees` | Doğrudan tutar veya adet | card_fees absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `mortgage_banking_abs` | `mortgage_banking` | Doğrudan tutar veya adet | mortgage_banking absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_gains_from_trading_and_securities_abs` | `net_gains_from_trading_and_securities` | Doğrudan tutar veya adet | net_gains_from_trading_and_securities absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `other_noninterest_income_abs` | `other_noninterest_income` | Doğrudan tutar veya adet | other_noninterest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `technology_telecommunications_and_equipment_abs` | `technology_telecommunications_and_equipment` | Doğrudan tutar veya adet | technology_telecommunications_and_equipment absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `occupancy_abs` | `occupancy` | Doğrudan tutar veya adet | occupancy absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `operating_losses_abs` | `operating_losses` | Doğrudan tutar veya adet | operating_losses absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `professional_and_outside_services_abs` | `professional_and_outside_services` | Doğrudan tutar veya adet | professional_and_outside_services absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `advertising_and_promotion_abs` | `advertising_and_promotion` | Doğrudan tutar veya adet | advertising_and_promotion absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `other_noninterest_expense_abs` | `other_noninterest_expense` | Doğrudan tutar veya adet | other_noninterest_expense absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `pretax_income_abs` | `pretax_income` | Doğrudan tutar veya adet | pretax_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_income_before_nci_abs` | `net_income_before_nci` | Doğrudan tutar veya adet | net_income_before_nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `net_income_nci_abs` | `net_income_nci` | Doğrudan tutar veya adet | net_income_nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## WFC_2026Q1

Geçmiş dayanak kalemleri: `interest_income_debt_securities`, `interest_income_loans_held_for_sale`, `interest_income_loans`, `interest_income_equity_securities`, `interest_income_other`, `interest_expense_deposits`, `interest_expense_short_term_borrowings`, `interest_expense_long_term_debt`, `interest_expense_other`, `noninterest_income_deposit_and_lending_fees`, `noninterest_income_investment_advisory_fees`, `noninterest_income_commissions_and_brokerage_fees`, `noninterest_income_investment_banking_fees`, `noninterest_income_card_fees`, `noninterest_income_mortgage_banking`, `noninterest_income_net_gains_trading_securities`, `noninterest_income_other`, `provision_for_credit_losses`, `personnel_expense`, `technology_telecommunications_equipment_expense`, `occupancy_expense`, `operating_losses`, `professional_and_outside_services_expense`, `advertising_and_promotion_expense`, `other_noninterest_expense`, `tax_rate`, `noncontrolling_interest_income`, `preferred_stock_dividends`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `interest_income_yoy` | `total_interest_income` | Yıllık büyüme | Total interest income YoY growth vs Q-4 baseline |
| `interest_expense_yoy` | `total_interest_expense` | Yıllık büyüme | Total interest expense YoY growth vs Q-4 baseline |
| `noninterest_income_yoy` | `total_noninterest_income` | Yıllık büyüme | Total noninterest income YoY growth vs Q-4 baseline |
| `provision_credit_losses_margin_delta_bps` | `provision_for_credit_losses / çapa: total_revenue` | Marj değişimi, baz puan | Provision for credit losses as % of total revenue, delta vs Q-4 baseline |
| `noninterest_expense_margin_delta_bps` | `total_noninterest_expense / çapa: total_revenue` | Marj değişimi, baz puan | Total noninterest expense as % of total revenue, delta vs Q-4 baseline |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `noncontrolling_interest_income_abs` | `noncontrolling_interest_income` | Doğrudan tutar veya adet | noncontrolling_interest_income absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `preferred_stock_dividends_abs` | `preferred_stock_dividends` | Doğrudan tutar veya adet | preferred_stock_dividends absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

## WMT_2026Q4

Geçmiş dayanak kalemleri: `net_sales`, `membership_and_other_income`, `cost_of_sales`, `operating_selling_general_and_administrative_expenses`, `interest_debt`, `interest_finance_lease`, `interest_income`, `other_gains_and_losses`, `tax_rate`, `noncontrolling_interest`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `net_sales_yoy` | `net_sales` | Yıllık büyüme | Net sales YoY growth rate vs Q-4 |
| `membership_and_other_income_yoy` | `membership_and_other_income` | Yıllık büyüme | Membership and other income YoY growth rate vs Q-4 |
| `cost_of_sales_margin_delta_bps` | `cost_of_sales / çapa: total_revenue` | Marj değişimi, baz puan | Cost of sales as % of total revenue, delta vs Q-4 |
| `opex_margin_delta_bps` | `operating_selling_general_and_administrative_expenses / çapa: total_revenue` | Marj değişimi, baz puan | Operating SG&A as % of total revenue, delta vs Q-4 |
| `interest_margin_delta_bps` | `interest_net / çapa: total_revenue` | Marj değişimi, baz puan | Net interest expense as % of total revenue, delta vs Q-4 |
| `other_gains_and_losses_margin_delta_bps` | `other_gains_and_losses / çapa: total_revenue` | Marj değişimi, baz puan | Other gains and losses as % of total revenue, delta vs Q-4 |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `noncontrolling_interest_abs` | `noncontrolling_interest` | Doğrudan tutar veya adet | noncontrolling_interest absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |

## XOM_2025Q4

Geçmiş dayanak kalemleri: `sales_and_other_operating_revenue`, `income_from_equity_affiliates`, `other_income`, `crude_oil_and_product_purchases`, `production_and_manufacturing_expenses`, `selling_general_and_admin_expenses`, `depreciation_and_depletion`, `exploration_expenses_including_dry_holes`, `non_service_pension_and_postretirement_benefit_expense`, `interest_expense`, `other_taxes_and_duties`, `pretax_income`, `nci`, `shares`, `tax_rate`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `sales_and_other_operating_revenue_yoy` | `sales_and_other_operating_revenue` | Yıllık büyüme | Sales and other operating revenue YoY growth rate vs Q-4 |
| `cogs_margin_delta_bps` | `total_costs_and_other_deductions / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | Cost of revenue margin delta vs Q-4 |
| `sga_margin_delta_bps` | `selling_general_and_admin_expenses / çapa: total_revenues_and_other_income` | Marj değişimi, baz puan | SG&A as % of total revenues margin delta vs Q-4 |
| `depreciation_and_depletion_yoy` | `depreciation_and_depletion` | Yıllık büyüme | Depreciation and depletion expense YoY growth rate vs Q-4 |
| `exploration_expenses_including_dry_holes_yoy` | `exploration_expenses_including_dry_holes` | Yıllık büyüme | Exploration expenses YoY growth rate vs Q-4 |
| `income_from_equity_affiliates_yoy` | `income_from_equity_affiliates` | Yıllık büyüme | income_from_equity_affiliates YoY growth rate vs Q-4 |
| `other_income_abs` | `other_income` | Doğrudan tutar veya adet | other_income absolute dollar value for the target quarter (predict the amount directly; 0 if none expected) |
| `non_service_pension_and_postretirement_benefit_expense_yoy` | `non_service_pension_and_postretirement_benefit_expense` | Yıllık büyüme | non_service_pension_and_postretirement_benefit_expense YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `other_taxes_and_duties_yoy` | `other_taxes_and_duties` | Yıllık büyüme | other_taxes_and_duties YoY growth rate vs Q-4 |
| `nci_abs` | `nci` | Doğrudan tutar veya adet | nci absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |
| `tax_rate` | `tax_rate` | Oranın doğrudan belirlenmesi | Effective GAAP tax rate for the target quarter (decimal, e.g. 0.14 = 14%; may be negative in a benefit quarter). Choose from the GAAP historical anchors provided; a discrete tax item can push it far from any of them. |

## XOM_2026Q1

Geçmiş dayanak kalemleri: `sales_and_other_operating_revenue`, `income_from_equity_affiliates`, `other_income`, `crude_oil_and_product_purchases`, `production_and_manufacturing_expenses`, `sga`, `depreciation_and_depletion`, `exploration_expenses`, `non_service_pension_expense`, `interest_expense`, `other_taxes_and_duties`, `income_taxes`, `noncontrolling_interests`, `shares`.

| Tahmin edilen sürücü | Bağlı kalem / çapa | İşlem türü | Kaynaktaki tanım |
|---|---|---|---|
| `revenue_yoy` | `total_revenues` | Yıllık büyüme | Total revenues and other income YoY growth rate vs Q-4 |
| `crude_oil_purchases_margin_delta_bps` | `crude_oil_and_product_purchases / çapa: total_revenues` | Marj değişimi, baz puan | Crude oil and product purchases as % of total revenues, delta vs Q-4 |
| `production_manufacturing_margin_delta_bps` | `production_and_manufacturing_expenses / çapa: total_revenues` | Marj değişimi, baz puan | Production and manufacturing expenses as % of total revenues, delta vs Q-4 |
| `sga_margin_delta_bps` | `sga / çapa: total_revenues` | Marj değişimi, baz puan | SG&A as % of total revenues, delta vs Q-4 |
| `depreciation_margin_delta_bps` | `depreciation_and_depletion / çapa: total_revenues` | Marj değişimi, baz puan | Depreciation and depletion as % of total revenues, delta vs Q-4 |
| `other_taxes_margin_delta_bps` | `other_taxes_and_duties / çapa: total_revenues` | Marj değişimi, baz puan | Other taxes and duties as % of total revenues, delta vs Q-4 |
| `exploration_expenses_yoy` | `exploration_expenses` | Yıllık büyüme | exploration_expenses YoY growth rate vs Q-4 |
| `non_service_pension_expense_yoy` | `non_service_pension_expense` | Yıllık büyüme | non_service_pension_expense YoY growth rate vs Q-4 |
| `interest_expense_yoy` | `interest_expense` | Yıllık büyüme | interest_expense YoY growth rate vs Q-4 |
| `income_taxes_abs` | `income_taxes` | Doğrudan tutar veya adet | income_taxes absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `noncontrolling_interests_abs` | `noncontrolling_interests` | Doğrudan tutar veya adet | noncontrolling_interests absolute dollar value for the target quarter (below-pretax line; predict directly, 0 if none expected). |
| `shares_abs` | `shares` | Doğrudan tutar veya adet | shares: diluted weighted-average share count for the target quarter (predict the count directly; drifts slowly with buybacks/issuance). |

