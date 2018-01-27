pytestlist=`find test/ -name '*[^__init__].py'`
python3 -m unittest $pytestlist -v
