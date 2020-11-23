
# floger::pg

floger::pg is the Previous Generation Firewall LOG viewER powered by Human correlation

in other words, floger pg is a log viewer with the objective to be uses
full for system and security administrators.
the  main philosophy of floger is not to avoid doing what needs to be  
done, but do it only once!

With floger you can apply filters to your firewall logs and aggregate in a
tree, adding information of the number of event by group, and apply
quick filters with a double click in the branches of the tree

floger is in the preliminary version 0.1.0 but new features are coming


##Log formats

Currently the next format are supported:
 - iptables-fwb: the iptables logs using the rule comment of fwbuilder ( RULE [number] -- [ACTION] )
 - syslog: the generic syslog format, really are a not a firewall log format, but is very useful
 - sophos-utm9: the logs generated by the sophos utm9 or Astaro firewalls, only is supported IPv4
  
You have other log formats? 
please, send me a example of your logs to define the parser  and be included future versions of floger

## Table filter

the more basic functionality of floger is to apply a filter based in
a regex expression to the main table of events, this filter is a coma separated
list of table fields ':' and regex:

``` action: DENY, rule: 6, dst: 1.1.2.2, dpt: 22 ```

to apply the filter, press enter.

floger remember your last filter, helping to you to do not write the same filter all the time.

currently, only <and> filters are supported but a more powerful filtering language is planed for future versions
  
## Tree groups

The main difference of floger with other log analyzers is the possibility 
of aggregate all the event in a tree, grouping by the different table labels,
to do it, you only need to define the label order in the line-edit in the top
of the tree, with a list separated by comas:

``` action,  rule,  dst, dpt,  rule ```

To apply the groups, press enter.

Also in the sorted groups, floger remember your last list, helping to you to do not write the same list all the time.

## Mappers

in complex infrastructures are very frequent to have a long list of ips and host, and no always exist a inverse dns resolution, 
to fight with this problem, you can add to floger mapper, this is a CSV file [ip];[host-namme-and-or-info], as example:
  
  ``` 1.1.1.1 ;www.acme.com - dmz server at VLAN 1001
  1.1.1.24;bigdb.acme.com - db server at VLAN 1001
  1.1.2.1;puppy.acme.com - fw red_net vip IP
  1.1.2.2;puppy1.acme.com - fw1 admin IP red_net
  1.1.2.3;puppy2.acme.com - fw2 admin IP red_net 
  ```
  
The mapper will populate a new field m_src and m_dst or similar fields based in the fields of the firewall.

## Config file

floger save all the configuration and historic files and filters in the config file:

``` ~/.config/floger/floger.conf ```

this is a json file, and can be edit, but floger will write to it to save the state of the last opened files, filters, orders, etc.



## You can help 

If you are using other firewall logs, and can send me a sample to analyze, I will try to include in future versions of floger.
You write your own regular expressions and added to the floger, please send me the patch to add to future versions.
Would you like to include some functionality, please send me your idea, your patch, ... to be analyzed or included in floger, 
any help are welcome!!! 




