## Pushups Logger



- open python shell in the root directory
```sh
python
```
- and then execute the below code:

```python
from pushups_logger import db, create_app

app = create_app()

with app.app_context():
    db.create_all()

exit()

```