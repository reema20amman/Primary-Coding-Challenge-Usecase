import json

data_file = '''
[
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]

'''

data = json.loads(data_file)
data                    // display data

pd.set_option('display.max_columns', None)

def udf_data_value(data, table_name):
    cnx = sqlite3.connect('C:/Users/USER/Downloads/Chinook_Sqlite.sqlite.db')
    data.to_sql(table_name, cnx)

    
def flatten_json(json_data, parent_key='', sep='_'):
    flattened_data = {}
    for key, value in json_data.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flattened_data.update(flatten_json(item, new_key + sep + str(i), sep=sep))
        else:
            flattened_data[new_key] = value
    return flattened_data

for i in data:
#     print(i)
    output = flatten_json(i)
#     display(output)

    df = pd.DataFrame([output])
    display(df)

table_data = udf_data_value(df, 'new_table')
