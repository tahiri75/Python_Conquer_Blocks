RBM_Serie_1_price = 20
RMB_Serie_Plus_price = 35
RBM_Todoterreno_price = 60
RBM_Serie_1_commission = 0.03
RMB_Serie_Plus_commission = 0.05
RBM_Todoterreno_commission = 0.07
RBM_Serie_1_vendidos = int(
    input("Cantidad de coches vendidos del modelo RBM Serie 1: ")
)
RMB_Serie_Plus_vendidos = int(
    input("Cantidad de coches vendidos del modelo RMB Serie Plus: ")
)
RBM_Todoterreno_vendidos = int(
    input("Cantidad de coches vendidos del modelo RBM Todoterreno: ")
)
total_price_RBM_Serie_1 = RBM_Serie_1_price * RBM_Serie_1_vendidos
total_price_RMB_Serie_Plus = RMB_Serie_Plus_price * RMB_Serie_Plus_vendidos
total_price_RBM_Todoterreno = RBM_Todoterreno_price * RBM_Todoterreno_vendidos
total_commission_RBM_Serie_1 = total_price_RBM_Serie_1 * RBM_Serie_1_commission
total_commission_RMB_Serie_Plus = total_price_RMB_Serie_Plus * RMB_Serie_Plus_commission
total_commission_RBM_Todoterreno = (
    total_price_RBM_Todoterreno * RBM_Todoterreno_commission
)
total_commission = (
    total_commission_RBM_Serie_1
    + total_commission_RMB_Serie_Plus
    + total_commission_RBM_Todoterreno
)
print(
    f"Total de comisión por ventas del modelo RBM Serie 1: {total_commission_RBM_Serie_1}"
)
print(
    f"Total de comisión por ventas del modelo RMB Serie Plus: {total_commission_RMB_Serie_Plus}"
)
print(
    f"Total de comisión por ventas del modelo RBM Todoterreno: {total_commission_RBM_Todoterreno}"
)
print(f"Total de comisión por ventas de todos los modelos: {total_commission}")
