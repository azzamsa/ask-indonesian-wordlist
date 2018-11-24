# scale number
function scale_between(unscaled_num, min_allowed, max_allowed, min, max) {
    scaled_num = int((max_allowed - min_allowed) * (unscaled_num - min) / (max - min) + min_allowed);

}

{
    scale_between($2, 1, 255, 271, 795050);
    print $1, scaled_num;

}
