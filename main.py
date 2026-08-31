import flet as ft

def main(page: ft.Page):
    # 設定最基本的視窗屬性
    page.title = "唱吧音訊一鍵替換助手"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 畫面只顯示最簡單的空殼提示文字，確保畫面能正常渲染
    page.add(
        ft.Text(
            value="唱吧空殼實驗 APK 運行中\n請至系統設定檢查權限狀態",
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="amber"
        )
    )

# Flet 的標準進入點
ft.app(target=main)