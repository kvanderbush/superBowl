import nflgame
from nflgame import *
from pprint import pprint
from itertools import islice
import csv

def take(n,iterable):
    return list(islice(iterable,n))

## I am not a computer programmer. I do not know what I'm doing
postseason = nflgame.games(2014,kind='POST')
sb = postseason[(len(postseason)-1)]

drives = sb.drives

def a(ob,sub):
    try:
        return ob.sub
    except:
        return '0'
    
playerrors = []
with open('playdata.csv','wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(('seq','drive_num','drive_result','drive_yds','quarter','time','team','position','play_desc','note','playid'))
    rowid = 1
    for d in drives:
        for p in d.plays:
            try:
                r = (rowid,d.drive_num,d.result,d.total_yds,p.time.quarter,p.time.clock,p.team,p.yardline.offset,p.desc,p.note,p.playid)
                writer.writerow(r)
                rowid+=1
            except BaseException as er:
                playerrors.append(p)
                print er

csvfile.close()
print 'data written to playdata.csv'
print len(playerrors), ' plays not written'

with open('players.csv','wb') as playerfile:
    wwriter = csv.writer(playerfile,dialect='excel')
    headers = ['playerid','name','team','jersey_number','position','height','weight','profile']
    wwriter.writerow(headers)
    err=[]
    for p in sb.players:
        try:
            pp = p.player
            val = (pp.playerid,pp.full_name,pp.team,pp.number,pp.position,pp.height,pp.weight,pp.profile_url)
            wwriter.writerow(val)
        except:
            err.append(p)
            pass
playerfile.close()
print "player data written to players.csv"
print len(err), " players not written"
def v(i,n):
    try:
        if i[n] is None:
            return '0'
        else:
            try:    
                return i[n]
            except:
                return '0'
    except:
        return '0'
with open('playstats.csv','wb') as datafile:
    dwriter = csv.writer(datafile,dialect='excel')
    head=['playid','playerid','defense_int', 'defense_int_yds', 'defense_pass_def', 'defense_qbhit', 'defense_sk', 'defense_sk_yds', 'defense_tkl', 'defense_tkl_loss_yds', 'defense_tkl_primary', 'first_down', 'kicking_all_yds', 'kicking_fga', 'kicking_fgm', 'kicking_fgm_yds', 'kicking_xpmade', 'kicking_yds', 'kickret_ret', 'kickret_yds', 'passing_att', 'passing_cmp', 'passing_cmp_air_yds', 'passing_incmp_air_yds', 'passing_int', 'passing_tds', 'passing_yds', 'penalty', 'penalty_yds', 'punting_tot', 'punting_yds', 'puntret_tot', 'puntret_yds', 'receiving_tds', 'receiving_yac_yds', 'receiving_yds', 'rushing_first_down', 'rushing_tds', 'rushing_yds', 'third_down_conv']
    dwriter.writerow(head)
    er=[]
    for d in drives:
        for p in d.plays:
            for e in p.events:
                try:
                    r = (p.playid,v(e,'playerid'), v(e,'defense_int'), v(e,'defense_int_yds'), v(e,'defense_pass_def'), v(e,'defense_qbhit'), v(e,'defense_sk'), v(e,'defense_sk_yds'), v(e,'defense_tkl'), v(e,'defense_tkl_loss_yds'), v(e,'defense_tkl_primary'), v(e,'first_down'), v(e,'kicking_all_yds'), v(e,'kicking_fga'), v(e,'kicking_fgm'), v(e,'kicking_fgm_yds'), v(e,'kicking_xpmade'), v(e,'kicking_yds'), v(e,'kickret_ret'), v(e,'kickret_yds'), v(e,'passing_att'), v(e,'passing_cmp'), v(e,'passing_cmp_air_yds'), v(e,'passing_incmp_air_yds'), v(e,'passing_int'), v(e,'passing_tds'), v(e,'passing_yds'), v(e,'penalty'), v(e,'penalty_yds'), v(e,'punting_tot'), v(e,'punting_yds'), v(e,'puntret_tot'), v(e,'puntret_yds'), v(e,'receiving_tds'), v(e,'receiving_yac_yds'), v(e,'receiving_yds'), v(e,'rushing_first_down'), v(e,'rushing_tds'), v(e,'rushing_yds'), v(e,'third_down_conv'))
                    dwriter.writerow(r)
                except BaseException as exception:
                    er.append(e)
                    print exception 
datafile.close()
print "play data written to playstats.csv"
print len(er), "events not written"
##
##players = {}
##for p in sb.players:
##    #p=pl.player
##    playerid = p.player.playerid
##    data={}
##    plays = {}
##    data.update(
##        {
##            'playername': p.player.full_name,
##            'team': p.player.team,
##            'number': p.player.number,
##            'position': p.player.position,
##            'height': p.player.height,
##            'weight': p.player.weight,
##            'profile': p.player.profile_url,
##            'plays': plays
##        })
##    players[playerid] = data
###pprint(players)
##ply = {}
##missed=[]
##for d in drives:
##    for p in d.plays:
##        for e in p.events:
##            try:
##                pp = e['playerid']
##                #pe={p.playid:e}
##                players[pp][plays].update(
##                    {p.playid:e}
##                    )
##            except:
##                missed.append(e)
##                continue
##print len(missed)," plays not appended"
#pprint(players)
##with open('playstats.csv','wb') as statfile:
##    writer = csv.DictWriter(statfile, dialect='excel')
##    writer.writerow(('seq','drive_num','drive_result','drive_yds','quarter','time','team','position','play_desc','note','playid'))
##    rowid = 1
##    for d in drives:
##        for p in d.plays:
##            try:
##                r = (rowid,d.drive_num,d.result,d.total_yds,p.time.quarter,p.time.clock,p.team,p.yardline.offset,p.desc,p.note,p.playid)
##                writer.writerow(r)
##                rowid+=1
##            except:
##                pass
##
##csvfile.close()


