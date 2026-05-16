import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- ページ設定 ---
st.set_page_config(
    page_title="大雪山 地下水保全データプロジェクト",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- カスタムCSS（ステータス表示用） ---
st.markdown("""
    <style>
    .status-green { color: #2e7d32; font-weight: bold; font-size: 1.1em;}
    </style>
""", unsafe_allow_html=True)

# --- ヘッダー領域 ---
st.title("大雪山 地下水保全データプロジェクト")
st.subheader("三千櫻酒造 様 専用コンソール（プロトタイプ）")
st.markdown(f"現在時刻: **{datetime.now().strftime('%Y年%m月%d日 %H:%M')}** | システム状態: <span class='status-green'>稼働中（正常）</span>", unsafe_allow_html=True)
st.markdown("---")

# --- カラムレイアウト設定（左:広域データ、中央:リアルタイム、右:AIアラート） ---
col_left, col_center, col_right = st.columns([1, 2, 1], gap="large")

# --- 左パネル：広域環境データ（OSINTモック） ---
with col_left:
    st.markdown("### 🌐 広域環境データ")
    st.caption("気象庁・国土交通省オープンデータ自動連携")
    
    st.metric(label="東川町 現在の気温", value="15.2 ℃", delta="+1.5 ℃")
    st.metric(label="忠別川 水位", value="1.45 m", delta="0.02 m")
    st.metric(label="過去24時間 降水量", value="0 mm", delta="0 mm")
    
    st.info("※このエリアのデータは公的機関の公開データから自動で収集され、酒造りの背景となる自然環境の状況として表示されます。")

# --- 中央メインパネル：地下水リアルタイムデータ ---
with col_center:
    st.markdown("### 💧 地下水リアルタイムデータ (仕込み水)")
    
    # メトリクス表示
    col_metric1, col_metric2 = st.columns(2)
    col_metric1.metric(label="現在の水温", value="12.4 ℃", delta="-0.2 ℃")
    col_metric2.metric(label="現在の水位", value="基準値内", delta="安定")
    
    st.markdown("#### 過去24時間の水温推移")
    
    # モックデータの生成（過去24時間のダミーデータ）
    now = datetime.now()
    times = [now - timedelta(hours=i) for i in range(24)]
    times.reverse()
    
    # 水温データ（12.4度前後で微変動する乱数）
    np.random.seed(42) # プロトタイプ表示用にシードを固定
    temp_data = 12.5 + np.random.randn(24) * 0.05
    temp_data[-1] = 12.4 # 現在値を12.4度に合わせる
    
    df = pd.DataFrame({
        "時間": times,
        "水温 (℃)": temp_data
    }).set_index("時間")
    
    # グラフ描画
    st.line_chart(df["水温 (℃)"], height=280)
    st.caption("※グラフは現在テスト用のデータを表示しています。実証実験にてセンサーを設置後、実際の実測値へ切り替わります。")

# --- 右パネル：AIアシスタント ---
with col_right:
    st.markdown("### 🤖 データ分析・通知")
    st.caption("過去の基準値に基づく予測とアドバイス")
    
    st.info("**【環境インサイト】春季の地下水安定期**\n\n大雪山系の主要な融雪はピークを越え、地下水脈への流入量が安定化しています。向こう1週間、急激な水温・水質の変動リスクは極めて低いと予測されます。")
    
    st.success("**【推奨アクション】**\n\n現在の仕込みにおいて、外部環境による水質変動の懸念はありません。通常の温度管理プロトコルを継続してください。")
    
    st.info("**【システム通知】**\n\n水位・水質ともに、過去の安定した基準値と比較して正常の範囲内を保っています。")