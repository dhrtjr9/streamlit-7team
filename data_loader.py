import pandas as pd

def data_loader():
    df = pd.read_csv('./ORIGIN_PAY.csv',names = ['기준년월','주문시간','주문명','광역시도명','주소명','결제종류'])
    df_seoul = df[df['광역시도명']=='서울특별시']
    df_seoul['위도'] = 0
    df_seoul['경도'] = 0

    df_seoul.loc[(df_seoul['주소명']=='영등포구'),'위도'] = 37.526045500975
    df_seoul.loc[(df_seoul['주소명']=='영등포구'),'경도'] = 126.89652510356

    df_seoul.loc[(df_seoul['주소명']=='서초구'),'위도'] = 37.484217490849
    df_seoul.loc[(df_seoul['주소명']=='서초구'),'경도'] = 127.03335749867

    df_seoul.loc[(df_seoul['주소명']=='금천구'),'위도'] = 37.456440659923
    df_seoul.loc[(df_seoul['주소명']=='금천구'),'경도'] = 126.89550733404

    df_seoul.loc[(df_seoul['주소명']=='은평구'),'위도'] = 37.604293500727
    df_seoul.loc[(df_seoul['주소명']=='은평구'),'경도'] = 126.91664195691

    df_seoul.loc[(df_seoul['주소명']=='구로구'),'위도'] = 37.495025886857
    df_seoul.loc[(df_seoul['주소명']=='구로구'),'경도'] = 126.88797161395

    df_seoul.loc[(df_seoul['주소명']=='도봉구'),'위도'] = 37.668701731992
    df_seoul.loc[(df_seoul['주소명']=='도봉구'),'경도'] = 127.04700675774

    df_seoul.loc[(df_seoul['주소명']=='강남구'),'위도'] = 37.490903970499
    df_seoul.loc[(df_seoul['주소명']=='강남구'),'경도'] = 127.03837557412

    df_seoul.loc[(df_seoul['주소명']=='동작구'),'위도'] = 37.512366991508
    df_seoul.loc[(df_seoul['주소명']=='동작구'),'경도'] = 126.93987199859

    df_seoul.loc[(df_seoul['주소명']=='양천구'),'위도'] = 37.516886961815
    df_seoul.loc[(df_seoul['주소명']=='양천구'),'경도'] = 126.86649931775

    df_seoul.loc[(df_seoul['주소명']=='서대문구'),'위도'] = 37.580979196767
    df_seoul.loc[(df_seoul['주소명']=='서대문구'),'경도'] = 126.90809849307

    df_seoul.loc[(df_seoul['주소명']=='관악구'),'위도'] = 37.478166304145
    df_seoul.loc[(df_seoul['주소명']=='관악구'),'경도'] = 126.95162849247

    df_seoul.loc[(df_seoul['주소명']=='관악구'),'위도'] = 37.557716552166
    df_seoul.loc[(df_seoul['주소명']=='관악구'),'경도'] = 127.15692258005

    df_seoul.loc[(df_seoul['주소명']=='관악구'),'위도'] = 37.6536180063
    df_seoul.loc[(df_seoul['주소명']=='관악구'),'경도'] = 127.05670272546

    df_seoul.loc[(df_seoul['주소명']=='관악구'),'위도'] = 35.211284547663
    df_seoul.loc[(df_seoul['주소명']=='관악구'),'경도'] = 128.98047886684

    return df_seoul