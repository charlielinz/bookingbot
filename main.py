import pathlib
import gspread
from booking_funcs import book_fermizhenxinfen, book_zhiyue

restaurant_to_name = {
    "fermizhenxinfen": "fermi真心粉",
    "zhiyue": "旨樂",
}
restaurant_to_booking_func = {
    "fermizhenxinfen": book_fermizhenxinfen,
    "zhiyue": book_zhiyue,
}

base_dir = pathlib.Path(__file__).resolve().parent
gc = gspread.service_account(filename=base_dir / ".service_account.json")


def start_booking(restaurant):
    sheet = gc.open(restaurant_to_name[restaurant])
    worksheet = sheet.get_worksheet(0)
    orders = worksheet.get_all_records()

    # TODO multiple thread
    for order in orders:
        booking_func = restaurant_to_booking_func[restaurant]
        booking_func(order)
