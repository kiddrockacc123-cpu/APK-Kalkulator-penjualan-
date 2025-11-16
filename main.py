from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 20

    TextInput:
        id: uang_awal
        hint_text: "Dana awal (kembalian)"
        input_filter: "float"

    TextInput:
        id: hasil_jual
        hint_text: "Hasil jualan toko"
        input_filter: "float"

    TextInput:
        id: pengeluaran
        hint_text: "Pengeluaran belanja"
        input_filter: "float"

    Button:
        text: "Hitung"
        size_hint_y: None
        height: 50
        on_release: app.hitung()

    Label:
        id: hasil
        text: ""
'''

class TokoApp(App):
    def build(self):
        return Builder.load_string(kv)

    def hitung(self):
        ui=self.root
        uang=float(ui.ids.uang_awal.text or 0)
        jual=float(ui.ids.hasil_jual.text or 0)
        keluar=float(ui.ids.pengeluaran.text or 0)
        total=uang + jual - keluar
        ui.ids.hasil.text=f"Total akhir: Rp {total:,.0f}"

TokoApp().run()
