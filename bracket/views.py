from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from bracket.models import Team, TeamStat

# Create your views here.

def home(request):
	model = TeamStat
	
	bracket_form = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
	
	south = TeamStat.objects.filter(region='South')
	east = TeamStat.objects.filter(region='East')
	midwest = TeamStat.objects.filter(region='Midwest')
	west = TeamStat.objects.filter(region='West')
	
	south_dict = {}
	east_dict = {}
	mw_dict = {}
	west_dict = {}
	
	def region_dict(region_dict, region_list):
		for teams in region_list:
			region_dict[teams.abbrev]={}
			region_dict[teams.abbrev]['rank']=teams.rank
			region_dict[teams.abbrev]['magic_no']=teams.magic_no
			region_dict[teams.abbrev]['id']=teams.id
	
	region_dict(south_dict, south)
	region_dict(east_dict, east)
	region_dict(mw_dict, midwest)
	region_dict(west_dict, west)
	
	south_order = []
	east_order = []
	mw_order = []
	west_order = []
	
	def ranking_list(region_dict, region_list):
		for values in bracket_form:
			for names in region_dict.keys():
				if region_dict[names]['rank']==str(values):
					region_list.extend([ [names, region_dict[names].get('rank'), float(region_dict[names].get('magic_no')), region_dict[names].get('id') ]])
				else:
					pass
	
	ranking_list(south_dict, south_order)
	ranking_list(east_dict, east_order)
	ranking_list(mw_dict, mw_order)
	ranking_list(west_dict, west_order)
	
	
	south_eight = []
	east_eight = []
	mw_eight = []
	west_eight = []
	
	def knock_out(region_list, winner_list, game_stop):
		
		#Enumerate helps me pick the the following team in the list
		for index in range(0,game_stop,2): 
	
			if region_list[index][2]== 0:
				winner_list.append(region_list[index+1])
			elif region_list[index+1][2]== 0:
				winner_list.append(region_list[index])
			elif region_list[index][2] > region_list[index+1][2]: 
				winner_list.append(region_list[index+1])
			elif region_list[index][2] > region_list[index+1][2]: 
				winner_list.append(region_list[index])
			else:
				winner_list.append(region_list[index])
			
				
	knock_out(south_order, south_eight,15 )
	knock_out(east_order, east_eight, 15 )
	knock_out(mw_order, mw_eight, 15 )
	knock_out(west_order, west_eight,15 )
	
	south_four = []
	east_four = []
	mw_four = []
	west_four = []
	
	knock_out(south_eight,south_four, 7 )
	knock_out(east_eight,east_four, 7 )
	knock_out(mw_eight,mw_four, 7 )
	knock_out(west_eight,west_four,7 )
	
	south_two = []
	east_two = []
	mw_two = []
	west_two = []
	
	knock_out(south_four,south_two, 3 )
	knock_out(east_four,east_two, 3 )
	knock_out(mw_four,mw_two, 3 )
	knock_out(west_four,west_two,3 )
	
	south_one = []
	east_one = []
	mw_one = []
	west_one = []
	
	knock_out(south_two,south_one, 1 )
	knock_out(east_two,east_one, 1 )
	knock_out(mw_two,mw_one, 1 )
	knock_out(west_two,west_one,1 )
	
	if east_one[0][2] < mw_one[0][2]:
		winner_top = east_one
	else:
		winner_top = mw_one
	
	if west_one[0][2] < south_one[0][2]:
		winner_bottom = west_one
	else:
		winner_bottom = south_one
		
	if winner_top[0][2] < winner_bottom[0][2]:
		champion = winner_top
	else:
		champion = winner_bottom
	
	return render_to_response("bracket_test.html", 
								locals(), 
								context_instance= RequestContext(request))
def viewTeam(request, id ):
	template_name = 'view_team.html'
	team_list = []
	titles = ['Graduation', 'Admissions', 'Basketball Scholarships', 'STEM Graduates' ]
	stats = [['male_grad_rate', 'female_grad_rate'], ['male_admin_rate', 'female_admin_rate'], ['male_bb_rate', 'female_bb_rate'], ['male_stem_rate', 'female_stem_rate']]
	 
	
	for data in TeamStat.objects.filter(id = id).values():
		for items in stats:
			team_list.extend([[data.get(items[0]),data.get(items[1])]])
	
	name = TeamStat.objects.filter(id = id)
	table_list = zip(titles, team_list)
	
	for data in TeamStat.objects.filter(id = id).values():
			region = data.get('region')
			

	top_names = TeamStat.objects.filter(region = region).order_by('magic_no')
	bottom_names = TeamStat.objects.filter(region = region).order_by('-magic_no')
	
	
	return render(request, template_name, {'table_list': table_list,'name':name, 'region': region, 'region_data': top_names[:3], 'region_bottom': bottom_names[:3]})

def Source(request):
	
	return render_to_response("sources.html", 
								locals(), 
								context_instance= RequestContext(request))