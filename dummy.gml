graph [
	directed 0
	node
	[
		id 1
		type "a"
	]
	node
	[
		id 2
		type "b"
	]
	node
	[
		id 3
		type "c"
	]
		node
	[
		id 4
		type "c"
	]
		node
	[
		id 5
		type "c"
	]
		node
	[
		id 6
		type "c"
	]
	edge
	[
		source 1
		target 2
		weight 1
	]
	edge
	[
		source 2
		target 3
		weight 3
	]
	edge
	[
		source 3
		target 1
		weight 2
	]
	edge
	[
		source 3
		target 4
		weight 4
	]
	edge
	[
		source 4
		target 5
		weight 2
	]
	edge
	[
		source 5
		target 6
		weight 1
	]
	edge
	[
		source 6
		target 4
		weight 3
	]
]