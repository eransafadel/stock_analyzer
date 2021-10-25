from finvizfinance.quote import finvizfinance


def check_float(potential_float:str):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


class MyStock:



    def __init__(self, ticker: str):
        self.ticker = ticker

        self.finance = finvizfinance(ticker).TickerFullInfo()['fundament']

        self.price = self.finance['Price']
        self.name = self.finance['Company']
        self.sector = self.finance['Sector']
        self.pe = [self.finance['P/E'], False, False]
        self.peg = [self.finance['PEG'], False, False]
        self.roe = [self.finance['ROE'].strip('%'), False, False]
        self.roi = [self.finance['ROI'].strip('%'), False, False]
        self.debt_eq = [self.finance['Debt/Eq'], False, False]
        self.p_fcf = [self.finance['P/FCF'], False, False]
        self.prof_margin = [self.finance['Profit Margin'].strip('%'), False, False]
        self.sales_q_q = [self.finance['Sales Q/Q'].strip('%'), False, False]
        self.eps_q_q = [self.finance['EPS Q/Q'].strip('%'), False, False]
        self.higher_price_this_year = [self.finance['52W High'].strip('%'), False, False]
        self.chart = finvizfinance("fb").TickerCharts()
        self.set_values()
        self.set_color()

    def set_values(self):
        self.pe[1] = check_float(self.pe[0])
        self.peg[1] = check_float(self.peg[0])
        self.roe[1] = check_float(self.roe[0])
        self.roi[1] = check_float(self.roi[0])
        self.debt_eq[1] = check_float(self.debt_eq[0])
        self.p_fcf[1] = check_float(self.p_fcf[0])
        self.prof_margin[1] = check_float(self.prof_margin[0])
        self.sales_q_q[1] = check_float(self.sales_q_q[0])
        self.eps_q_q[1] = check_float(self.eps_q_q[0])
        self.higher_price_this_year[1] = check_float(self.higher_price_this_year[0])
        self.over_all = [0, False]

    def inc_over_all(self):
            self.over_all[0] += 1

    def set_color(self):
        if check_float(self.pe[0]) and float(self.pe[0]) < 22.5:
            self.pe[2]= True
            self.inc_over_all()

        if check_float(self.peg[0]) and float(self.peg[0]) < 1.5:
            self.peg[2] = True
            self.inc_over_all()

        if check_float(self.roe[0]) and float(self.roe[0]) > 15:
            self.roe[2] = True
            self.inc_over_all()

        if check_float(self.roi[0]) and float(self.roi[0]) > 15:
            self.roi[2] = True
            self.inc_over_all()

        if check_float(self.debt_eq[0]) and float(self.debt_eq[0]) < 1:
            self.debt_eq[2] = True
            self.inc_over_all()

        if check_float(self.p_fcf[0]) and float(self.p_fcf[0]) < 20:
            self.p_fcf[2] = True
            self.inc_over_all()

        if check_float(self.prof_margin[0]) and float(self.prof_margin[0]) > 10:
            self.prof_margin[2] = True
            self.inc_over_all()

        if check_float(self.sales_q_q[0]) and float(self.sales_q_q[0]) > 10:
            self.sales_q_q[2] = True
            self.inc_over_all()

        if check_float(self.eps_q_q[0]) and float(self.eps_q_q[0]) > 10:
            self.eps_q_q[2] = True
            self.inc_over_all()

        if check_float(self.higher_price_this_year[0]) and float(self.higher_price_this_year[0]) < -10:
            self.higher_price_this_year[2] = True
            self.inc_over_all()

        self.over_all[1] = self.over_all[0] >= 7



    def to_json(self)->dict:
        values = {
            'P/E:': self.pe[0],
            'PEG:': self.peg[0],
            'ROE:': self.roe[0] + '%',
            'ROI:': self.roi[0] + '%',
            'Debt/Eq:': self.debt_eq[0] + '%',
            'P/FCF:': self.p_fcf[0] + '%',
            'Profit Margin:': self.prof_margin[0] + '%',
            'Sales Q/Q:': self.sales_q_q[0] + '%',
            'EPS Q/Q:': self.eps_q_q[0] + '%',
            '52W High:': self.higher_price_this_year[0] + '%',
            '\t Over All': self.over_all[0]

        }
        return values

    def to_json_color(self)->dict:
        b = {
            'P/E': self.pe[2],
            'PEG': self.peg[2],
            'ROE': self.roe[2],
            'ROI': self.roi[2],
            'Debt/Eq': self.debt_eq[2],
            'P/FCF': self.p_fcf[2],
            'Profit Margin': self.prof_margin[2],
            'Sales Q/Q': self.sales_q_q[2],
            'EPS Q/Q': self.eps_q_q[2],
            '52W High': self.higher_price_this_year[2],
            'Over All': self.over_all[1]

        }
        return b
