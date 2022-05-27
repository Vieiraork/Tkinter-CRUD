from tkinter import Label, Tk, Button, X, Entry, StringVar, ttk
from tkinter.messagebox import showerror, showinfo
from produtos_dao.produtos import Produtos


class Window:
    def __init__(self) -> None:
        # Variables and Objects Instances
        self.__new_price = 0.0
        self.products = Produtos()

        # Window
        self.window = Tk()
        self.window.geometry("600x600")
        self.window.title('Registro de Produtos')
        # Variables for "input" Entry
        self.product = StringVar()
        self.price = StringVar()

        # Label and Entry definition
        product_label = Label(self.window, {'text': 'Produto'})
        product_label.pack()
        product_entry = Entry(self.window, textvariable=self.product, width=50)
        product_entry.pack({'fill': None})

        # Label and Entry definition
        price_label = Label(self.window, {'text': 'Preço'})
        price_label.pack()
        price_entry = Entry(self.window, textvariable=self.price, width=30)
        price_entry.pack()

        # Button declaration
        button = Button(self.window, {'text': 'Cadastrar', 'bg': 'green', 'fg': 'white'},
                        command=lambda: self.save_products(self.product.get(), self.price.get())
                        if self.product.get() != '' and self.price.get() != '' else "",
                        width=10)
        button.pack(pady=10)

        separator_label2 = Label(self.window, {'text': ''})
        separator_label2.pack({'fill': X})

        self.treeview = ttk.Treeview(self.window)

        table_label = Label(self.window, {'text': 'Tabela de produtos'})
        table_label.pack()
        # Format Columns
        self.treeview["columns"] = ("ID", "Produto", "Preço")
        self.treeview.column('#0', width=80, minwidth=25)
        self.treeview.column('ID', width=40, minwidth=3)
        self.treeview.column('Produto', width=240, minwidth=25)
        self.treeview.column('Preço', width=120, minwidth=5)

        # Create Headings
        self.treeview.heading("#0", text='Label')
        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Produto', text='Produto')
        self.treeview.heading('Preço', text='Preço')

        self.treeview.pack()

        delete_button = Button(self.window, {'text': 'Deletar Selecionado', 'bg': 'red', 'fg': 'white'},
                               command=lambda: self.delete_products())
        delete_button.pack(pady=10)

    def save_products(self, product: str, price: str) -> None:
        if self.validate_price(price):
            if self.products.insert(product, self.__new_price):
                self.product.set('')
                self.price.set('')
                self.treeview.delete()
                self.populate_table()
                showinfo('Sucesso', 'Produto cadastrado com sucesso.')
            else:
                showerror('Erro', 'Não foi possível inserir o produto.')

    def delete_products(self) -> None:
        table_data = self.treeview.selection()
        if len(table_data) > 0:
            if self.products.delete(int(table_data[0])):
                showinfo('Produto excluido', 'Produto excluído com sucesso.')
                self.populate_table()
            else:
                showerror('Falha na exclusão', 'Por algum motivo não foi possível excluir o item selecionado.')

    def validate_price(self, price: str) -> bool:
        price = price.replace(',', '.')
        try:
            self.__new_price = float(price)
        except Exception as e:
            showerror('Valor incorreto', 'Não foi possível associar o valor digitado a um valor monetário.')
            return False
        else:
            return True

    def populate_table(self) -> None:
        self.clear_table_data()
        selecao_produtos = self.products.select_data()
        for produto in selecao_produtos:
            self.treeview.insert('', index='end', text='Produto', iid=produto[0],
                                 values=(produto[0], produto[1], produto[2]))

    def clear_table_data(self) -> None:
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def run(self) -> None:
        self.window.mainloop()
