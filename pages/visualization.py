import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as img

def main_image(df_seoul):
    f,ax=plt.subplots(2,1,figsize=(18,18))
    sns.barplot(data=df_seoul,x='주소명',y='결제종류',estimator=sum, ci=None,ax=ax[0,])
    ax[0,].set_title('서울시 세부지역별 주문상품종류',fontsize=20)
    ax[0,].set_xticklabels(df_seoul['주소명'].dropna().unique(),rotation=-90)

    df_guro=df_seoul[df_seoul['주소명']=='구로구']

    x=df_guro.groupby(by='주문명')['결제종류'].sum().sort_values(ascending=False).index
    y=df_guro.groupby(by='주문명')['결제종류'].sum().sort_values(ascending=False)
    colors=sns.color_palette('hls',len(x))
    ax[1,].pie(y,labels=x,autopct='%.1f%%',colors=colors)
    ax[1,].set_title('구로구 주문상품별 카드이용건수',fontsize=20)
    ax[1,].legend(bbox_to_anchor=(0,1))
    plt.savefig('./main_image.png')
    main_image = img.imread('./main_image.png')
    return main_image