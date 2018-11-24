# remove short word
if( length($1) <= 1 ){ # remove short word
    next;
}
print $0;

# remove sites
if( $1 ~ /\.com$|\.id$|\.org$/){ # remove date
    next;
}
print $0;

# remove digit
if( $1 ~ /[0-9]$|[0-9]{2-10}$/){ # remove date
    next;
}
print $0;

# remove date
if( $1 ~ /[0-9]|[0-9]{2}\/[0-9]|[0-9]{2}\/[0-9]|[0-9]{2}/){ # remove date
    next;
}
print $0;
