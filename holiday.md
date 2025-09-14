# Non-Weather Events

Non-weather events are automatically loaded from the `holiday.json` file and any other files matching the pattern `holiday_*.json`.  The JSON file format is described below. The loading process can be monitored via the console.

**Example Output:**
```
Loaded 1 of 'Holidays' from './holiday.json'
Loaded 12 of 'Birthdays' from './holiday_birthdays.json'
```




## Holidays JSON Documentation

This section describes the structure and meaning of the **Holidays** JSON file.

---

### Root Object

- **title** (`string`): The title of the dataset.  
  Example: `"Holidays"`

- **data** (`array`): A list of holiday event objects. Each entry contains details about a single holiday.

---

### Holiday Event Object

Each object inside the `data` array has the following fields:

| Field       | Type     | Description                                                                 | Example     |
|-------------|----------|-----------------------------------------------------------------------------|-------------|
| `date`      | string   | The date of the holiday (day and month format).                             | `"24.12"`   |
| `sprite`    | string   | The identifier for the sprite related to the holiday.                | `"santa"`   |
| `index`     | integer  | A numeric index of the sprite.                     | `0`         |
| `time`      | string   | The starting time of the holiday event (24h format).                         | `"11:00"`   |
| `yoffset`   | integer  | Vertical offset for sprite positioning.                                      | `32`        |
| `xoffset`   | integer  | Horizontal offset for sprite positioning.                                    | `-40`       |
| `stayhours` | integer  | Duration (in hours) the holiday event lasts.                                 | `3`         |
| `text`      | string   | A human-readable name or label for the holiday.                              | `"Christmas"` |

---

### Example JSON

```json
{
  "title": "Holidays",
  "data": [
    {
      "date": "24.12",
      "sprite": "santa",
      "index": 0,
      "time": "11:00",
      "yoffset": 32,
      "xoffset": -40,
      "stayhours": 3,
      "text": "Christmas"
    }
  ]
}
