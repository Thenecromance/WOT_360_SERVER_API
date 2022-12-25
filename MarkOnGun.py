
################################
#python 2.7 this part of code should be the same as the modpack core hash algoritm
################################

# import hashlib
# # from tabnanny import check

# def hash_params(arg_dict,salt):
#     keys = arg_dict.keys()
#     keys.sort()
#     checkcontent=''
#     for _k in keys:
#         _v= arg_dict.get(_k)
#         checkcontent+=(_k+'='+_v+'&')
#     checkcontent+=salt
#     # print(checkcontent)
#     result = hashlib.md5(checkcontent).hexdigest()
    
#     # print(result)
#     return result

# def search_tanks_mog(tankid , percentile ='100'):
#     args_dict={}
#     args_dict['_t']='1647769686'
#     args_dict['percentile']=percentile
#     args_dict['distribution']='xp'
#     args_dict['tankId']=tankid
#     args_dict['sign']=  hash_params(args_dict,'WOT.ASSIST.MODS.360WJ')

#     keys = args_dict.keys()
#     keys.sort()
#     checkcontent='https://tbox.wot.360.cn/WotArenaData/getTankMastery?'
#     for _k in keys:
#         _v= args_dict.get(_k)
#         checkcontent+=(_k+'='+_v+'&')
#     print(checkcontent)



################################
#python 3.9 version 
################################
import hashlib
import urllib.request

def hash_params(params, salt ='WOT.ASSIST.MODS.360WJ'):
    '''
    world of tanks(360 Server)'s encrypt algorithm
    @params 
    @salt this value could only be 
    '''
    keys = params.keys() 
    keys= sorted(keys)
    print("sorted value :%s"% keys)
    md5_str=''
    for key in keys:
        value = params[key]
        md5_str+=(key+'='+value+'&')
    md5_str+=salt
    obj = hashlib.md5()
    obj.update(md5_str.encode())
    hashedValue =obj.hexdigest()
    print("origin params: " + md5_str)
    print("hashed:"+hashedValue)
    # hashedValue = hashlib.md5(checkContent).hexdigest()
    return hashedValue

def search_tanks_mog(tankid , percentile ='100'):
    '''
    how to use the hash_params
    
    @return here will return an json as response, in response 'all' section will only show the data from 1 to 95, above 95 need to get by percent 
    '''
    params ={}
    params['_t']='1647769686'           #don't need to care about this, they will never check 
    params['percentile']=percentile     #TanksMastery percent 
    params['distribution']='xp'         
    params['tankId']=tankid             #tank id which could get it from the other way
    params['sign']=  hash_params(params) # this sign it will be check
    
    keys = params.keys()
    keys= sorted(keys)
    url='https://tbox.wot.360.cn/WotArenaData/getTankMastery?'
    for key in keys:
        value = params[key]
        url+=(key+'='+value+'&')
        
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data  = response.read().decode('utf-8')
    return data

data = search_tanks_mog('57937')
print(data)