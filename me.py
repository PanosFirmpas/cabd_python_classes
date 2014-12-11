import random

d={}

with open('./E_zfin_gene_alias_2014.12.08.gff3','r') as gff:
	for line in gff:
		if not line.startswith('#') and len(line) >1:
			cols = line.rstrip().split('\t')
			
			chromosome = cols[0]
			if not chromosome.startswith('Zv9'):
				chromosome = 'chr'+chromosome

			start,end = cols[3:5]
			
			gid = cols[8].split(';')[0].split('=')[1]

			d[gid] = {'chromosome': chromosome,
					  'start': start,
					  'end': end}



			


			
with open('./gene_association.zfin','r') as zfin:
	for line in zfin:
		if not line.startswith('!') and len(line) >1:
			cols = line.rstrip().split('\t')
			
			d.get(cols[1],{})['go'] = cols[4]


# for k,v in d.items():
# 	if 'go' in v:
# 		print '{}\t{}\t{}\t{}\t{}'.format(
# 											v['chromosome'],
# 											v['start'],
# 											v['end'],
# 											k,
# 											v['go']
# 												)


pop = d.keys()

for i in range(10):
	s = random.sample(pop,500)
	with open('./random{}.bed'.format(i),'w') as fo:
		for k in s:
			fo.write('{}\n'.format(k))
			
