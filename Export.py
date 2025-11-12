from bs4 import BeautifulSoup

from spire.xls import Workbook, ExcelVersion

# Пример HTML с объединенными ячейками (colspan/rowspan)

html = """

<>

"""

# Парсинг HTML и нахождение первой таблицы

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")

# Инициализация Excel

workbook = Workbook()

sheet = workbook.Worksheets[0]

# Отслеживание объединенных ячеек для пропуска их позже

skip_cells = set()

# Цикл по HTML-строкам и ячейкам

for row_idx, row in enumerate(table.find_all("tr")):

    col_idx = 1  # Столбцы Excel начинаются с 1

    for cell in row.find_all(["th", "td"]):

        # Пропуск уже объединенных ячеек

        while (row_idx + 1, col_idx) in skip_cells:

            col_idx += 1

        # Получение значений colspan/rowspan (по умолчанию 1, если не указано)

        colspan = int(cell.get("colspan", 1))

        rowspan = int(cell.get("rowspan", 1))

        # Запись значения ячейки в Excel

        sheet.Range[row_idx + 1, col_idx].Text = cell.get_text(strip=True)

        # Объединение ячеек, если colspan/rowspan > 1

        if colspan > 1 or rowspan > 1:

            end_row = row_idx + rowspan

            end_col = col_idx + colspan - 1

            sheet.Range[row_idx + 1, col_idx, end_row, end_col].Merge()

            # Отметьте объединенные ячейки для пропуска

            for r in range(row_idx + 1, end_row + 1):

                for c in range(col_idx, end_col + 1):

                    if r != row_idx + 1 or c != col_idx:  # Пропустить основную ячейку

                        skip_cells.add((r, c))

        col_idx += colspan

# Автоматическая подстройка ширины столбцов

sheet.AllocatedRange.AutoFitColumns()

# Сохранение в Excel

workbook.SaveToFile("MergedCellsToExcel.xlsx", ExcelVersion.Version2016)

workbook.Dispose()