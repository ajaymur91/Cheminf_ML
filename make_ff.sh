tail -n +2 index_iupac_smiles.txt > index_iupac_smiles
while read p
do
#	echo "$p"
	arg1=$(echo $p | awk '{print $3}')
	arg2=$(echo $p | awk '{print $1}')
	echo $arg1 $arg2
	python create_gmx.py $arg1 $arg2
done <index_iupac_smiles




