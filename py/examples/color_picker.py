# Form / Color Picker
# No description available.
# ---
from telesync import Q, listen, ui


async def main(q: Q):
    if q.args.show_inputs:
        q.page['example'].items = [
            ui.text(f'color={q.args.color}'),
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['example'] = ui.form_card(box='1 1 4 10', items=[
            ui.color_picker(name='color', label='Pick a color', value='#F25F5C'),
            ui.button(name='show_inputs', label='Submit', primary=True),
        ])
    await q.page.push()


if __name__ == '__main__':
    listen('/demo', main)