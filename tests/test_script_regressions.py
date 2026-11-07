"""Regression expectations transcribed from the tracked KAP source cells."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import pandas as pd
import pytest
from parse_and_build_dataset import extract_rows_from_biff8, parse_financial_rows, detect_unit_multiplier
from rebuild_dataset import extract_extra, quarterize
ROOT = Path(__file__).resolve().parents[1]

@pytest.mark.parametrize('name,revenue,profit', [
    ('CLEBI_2013_Q1',102192118,-11160029),
    ('SARKY_2014_Q1',670275819,9076707),
    ('RYSAS_2010_Q1',49349642,3215357),
])
def test_current_three_month_column_survives_blank_ytd(name,revenue,profit):
    meta,rows=extract_rows_from_biff8(ROOT/'data/kap_raw_xls'/f'{name}.xls')
    f=parse_financial_rows(rows,1)
    assert f['T01_hasilat_3m_raw']==revenue
    assert f['T07_donem_net_kari_3m_raw']==profit

@pytest.mark.parametrize('name,expected', [
    ('AEFES_2011_Q1',-25227),('BIMAS_2011_Q1',149214),
    ('AYGAZ_2010_Q1',143828),('RYSAS_2010_Q1',-1602377),
    ('ARCLK_2010_Q1',288611),
])
def test_verified_operating_cash_total_labels(name,expected):
    _,rows=extract_rows_from_biff8(ROOT/'data/kap_raw_xls'/f'{name}.xls')
    f=parse_financial_rows(rows,1)
    f.update(extract_extra(rows,1))
    assert f['T15_isletme_nakit_akisi_ytd']==expected


def test_q1_three_month_is_valid_q1_and_prior_ytd_for_q2():
    d=pd.DataFrame(dict(ticker=['A','A'],year=[2020]*2,quarter=[1,2],
        consolidation=['solo']*2,currency=['TRY']*2,price_level_date=['nominal']*2,
        revenue_ytd=[None,30],revenue_3m_raw=[10,None]))
    assert quarterize(d,'revenue').tolist()==[10,20]


def test_pre_tax_profit_is_not_tax_expense():
    f=parse_financial_rows([('Gelir Tablosu',None,None),
        ('Sürdürülen Faaliyetler Vergi Öncesi Karı/Zararı',100,30),
        ('Sürdürülen Faaliyetler Vergi Gideri/Geliri',-20,-6)],1)
    assert f['T06_vergi_gideri_geliri_ytd']==-20
    assert f['T06_vergi_gideri_geliri_3m_raw']==-6


def test_tax_total_requires_both_reported_components():
    rows=[('Gelir Tablosu',None,None),
        ('- Dönem Vergi Gelir/Gideri',-32890,None)]
    assert parse_financial_rows(rows,1000)['T06_vergi_gideri_geliri_ytd'] is None
    rows.append(('- Ertelenmiş Vergi Gelir/Gideri',5328,None))
    assert parse_financial_rows(rows,1000)['T06_vergi_gideri_geliri_ytd']==-27562000
