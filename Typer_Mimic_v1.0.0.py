
import pyautogui
import time

#more text


# struct group_info init_groups = { .usage = ATOMIC_INIT(2) };
# struct group_info *groups_alloc(int gidsetsize){
#    struct group_info *group_info;
#    int nblocks;
#    int a;

#    nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
#    /* Make sure we always allocate at least one indirect block pointer */
#    nblocks = nblocks ? : 1;
#    group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
#    if (!group_info)
#       return NULL;
#    group_info->ngroups = gidsetsize;
#    group_info->nblocks = nblocks;
#    atomic_set(&group_info->usage, 1);

#    if (gidsetsize <= NGROUPS_SMALL)
#       group_info->blocks[0] = group_info->small_block;
#    else {
#       for (a = 0; a < nblocks; a++) {
#          gid_t *b;
#          b = (void *)__get_free_page(GFP_USER);
#          if (!b)
#             goto out_undo_partial_alloc;
#          group_info->blocks[a] = b;
#       }


text="""   }
   return group_info;

out_undo_partial_alloc:
   while (--a >= 0) {
      free_page((unsigned long)group_info->blocks[a]);
   }
   kfree(group_info);
   return NULL;
}

EXPORT_SYMBOL(groups_alloc);

void groups_free(struct group_info *group_info)
{
   if (group_info->blocks[0] != group_info->small_block) {
      int a;
      for (a = 0; a < group_info->nblocks; a++)
"""




#more text
#          free_page((unsigned long)group_info->blocks[a]);
#    }
#    kfree(group_info);
# }

# EXPORT_SYMBOL(groups_free);

# /* export the group_info to a user-space array */
# static int groups_to_user(gid_t __user *grouplist,
#            const struct group_info *group_info)
# {
#    int a;
#    unsigned int count = group_info->ngroups;

#    for (a = 0; a < group_info->nblocks; a++) {
#       unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
#       unsigned int len = cp_count * sizeof(*grouplist);

#       if (copy_to_user(grouplist, group_info->blocks[a], len))
#          return -EFAULT;

#       grouplist += NGROUPS_PER_BLOCK;
#       count -= cp_count;
#    }
#    return 0;
# }

# /* fill a group_info from a user-space array - it must be allocated already */
# static int groups_from_user(struct group_info *group_info,
#     gid_t __user *grouplist)
# {
#    int a;
#    unsigned int count = group_info->ngroups;

#    for (a = 0; a < group_info->nblocks; a++) {
#       unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
#       unsigned int len = cp_count * sizeof(*grouplist);

#       if (copy_from_user(group_info->blocks[a], grouplist, len))
#          return -EFAULT;

#       grouplist += NGROUPS_PER_BLOCK;
#       count -= cp_count;
#    }
#    return 0;
# }

# /* a simple Shell sort */
# static void groups_sort(struct group_info *group_info)
# {
#    int base, max, stride;
#    int gidsetsize = group_info->ngroups;

#    for (stride = 1; stride < gidsetsize; stride = 3 * stride + 1)
#       ; /* nothing */
#    stride /= 3;

#    while (stride) {
#       max = gidsetsize - stride;
#       for (base = 0; base < max; base++) {
#          int left = base;
#          int right = left + stride;
#          gid_t tmp = GROUP_AT(group_info, right);

#          while (left >= 0 && GROUP_AT(group_info, left) > tmp) {
#             GROUP_AT(group_info, right) =

#text from hacker typer

#list of delay characters, add to @delay_keys below
NEWLINE={"\n"}
SPECIAL_KEYS={'!','@','#','$','%','^','&','*','(',')','_','+','{','}','[',']','/',':',';','"','=','-'}
DELAY=SPECIAL_KEYS | NEWLINE

# add wait here for keys with unique delay
tabSize=3
typeInterval=0.08
specialInterval=0.09
waitTab=0.1
waitChange=0.08 #change to word
waitNewline=0.20
waitSpecial=0.15

word=""
tab=""
special_group=""
previous_key=""

time.sleep(6)
for key in text:
   # print("key '" + key + "'")
   print("word = '" + word + "'")
   # print("tab = '" + tab + "'")
   # print("previous = '" + previous + "'")
   
   if previous_key in SPECIAL_KEYS and previous_key == key: #for grouping specials so consecutive specials are written fast
      special_group += key 
      print("added special to group")
   elif key not in SPECIAL_KEYS or previous_key != key: #either not in special (is in space) or key not = previous; when don't need add anymore, then write
      if len(special_group) > 0:
         time.sleep(waitSpecial)
         pyautogui.write(special_group, interval=specialInterval)
         print("wrote special")
         special_group=""
   if len(special_group) == 0 and key in SPECIAL_KEYS:  #after word is written, set first letter of special_group
      special_group = key
   previous_key = key

   if " " in key: #if at space, will repeat until not at space
      tab += key # add space to tab
      print("added space to tab")
   else: # all space is grouped to check size (possibly still at space)
      while len(tab) >= tabSize: #deletes all tabs in tab and for each tab deleted, write one tab
         time.sleep(waitTab)
         pyautogui.press("tab")
         tab = tab.replace(" ", '', tabSize)
         print("pressed tab, removed tab")
      if 0 < len(tab) < tabSize: # add spaces remaining to word (to be typed in later)
         word += tab
         print("added space to word")
      tab="" #reset tab

      if key in DELAY: # if at key with delay
         if len(word) > 0: #don't write unless needed; decreases speed otherwise
            print("at special or newline")
            time.sleep(waitChange) 
            pyautogui.write(word, interval=typeInterval) # writes word (includes spacing)
            print("wrote word")
            word="" #resets word
#! @delay_keys
         if key in NEWLINE: #if at newline, write newline
            print("at newline")
            time.sleep(waitNewline)
            pyautogui.write(key)

      elif " " not in key: #if at key, accounts for if still at a space
         print("added key") 
         word += key

