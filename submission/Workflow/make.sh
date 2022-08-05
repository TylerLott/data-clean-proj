#!/usr/bin/env bash

# set variables
source settings.sh

# create output directories
mkdir -p $FACTS_DIR
mkdir -p $VIEWS_DIR
mkdir -p $RESULTS_DIR

# export YW model facts
$YW_CMD model $SCRIPT_DIR/data_cleaning.py \
        -c extract.language=python \
        -c extract.factsfile=$FACTS_DIR/yw_extract_facts.P \
        -c model.factsfile=$FACTS_DIR/yw_model_facts.P \
        -c query.engine=xsb

# materialize views of YW facts
$QUERIES_DIR/materialize_yw_views.sh > $VIEWS_DIR/yw_views.P

# generate reconfacts.P to facts/ folder from the run.yaml which is exported from run_manager (matlab client)sqlite database
# $YW_MATLAB_RECON_CMD recon $SCRIPT_DIR/C3_C4_map_present_NA_with_comments.m \
#         -c extract.language=matlab \
#         -c recon.matlab.exportfile=recon/run.yaml \
#         -c recon.factsfile=facts/reconfacts.P \
#         -c recon.finderclass=org.yesworkflow.matlab.MatlabResourceFinder \
#         -c query.engine=xsb

# draw complete workflow graph
$QUERIES_DIR/render_complete_wf_graph.sh > $RESULTS_DIR/complete_wf_graph.gv
dot -Tpdf $RESULTS_DIR/complete_wf_graph.gv > $RESULTS_DIR/complete_wf_graph.pdf
dot -Tsvg $RESULTS_DIR/complete_wf_graph.gv > $RESULTS_DIR/complete_wf_graph.svg

# draw complete workflow graph with URI template
$YW_CMD graph $SCRIPT_DIR/data_cleaning.py \
        -c graph.view=combined \
        -c graph.layout=tb \
        > $RESULTS_DIR/complete_wf_graph_uri.gv
dot -Tpdf $RESULTS_DIR/complete_wf_graph_uri.gv > $RESULTS_DIR/complete_wf_graph_uri.pdf
dot -Tsvg $RESULTS_DIR/complete_wf_graph_uri.gv > $RESULTS_DIR/complete_wf_graph_uri.svg

# list workflow outputs
$QUERIES_DIR/list_workflow_outputs.sh > $RESULTS_DIR/workflow_outputs.txt


##############
#   Q1_pro   #
##############

# # draw worfklow graph upstream of C3_fraction_data
# productName="C3_fraction_data"
# $QUERIES_DIR/render_wf_graph_upstream_of_data_q1.sh \'$productName\' > $RESULTS_DIR/wf_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.svg

# # draw worfklow graph upstream of C4_fraction_data
# productName="C4_fraction_data"
# $QUERIES_DIR/render_wf_graph_upstream_of_data_q1.sh \'$productName\' > $RESULTS_DIR/wf_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.svg

# # draw worfklow graph upstream of Grass_fraction_data
# productName="Grass_fraction_data"
# $QUERIES_DIR/render_wf_graph_upstream_of_data_q1.sh \'$productName\' > $RESULTS_DIR/wf_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_upstream_of_$productName.gv > $RESULTS_DIR/wf_upstream_of_$productName.svg


##############
#   Q2_pro   #
##############

# # list script inputs upstream of output data C3_fraction_data
# productName="C3_fraction_data"
# $QUERIES_DIR/list_inputs_upstream_of_data_q2.sh \'$productName\' $productName > $RESULTS_DIR/inputs_upstream_of_$productName.txt

# # list script inputs upstream of output data C4_fraction_data
# productName="C4_fraction_data"
# $QUERIES_DIR/list_inputs_upstream_of_data_q2.sh \'$productName\' $productName > $RESULTS_DIR/inputs_upstream_of_$productName.txt

# # list script inputs upstream of output data Grass_fraction_data
# productName="Grass_fraction_data"
# $QUERIES_DIR/list_inputs_upstream_of_data_q2.sh \'$productName\' $productName > $RESULTS_DIR/inputs_upstream_of_$productName.txt


# ##############
# #   Q3_pro   #
# ##############

# # draw worfklow graph downstream of mean_precip
# productName="mean_precip"
# $QUERIES_DIR/render_wf_graph_downstream_of_data_q3.sh $productName > $RESULTS_DIR/wf_downstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.svg

# # draw worfklow graph downstream of mean_airtemp
# productName="mean_airtemp"
# $QUERIES_DIR/render_wf_graph_downstream_of_data_q3.sh $productName > $RESULTS_DIR/wf_downstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.svg

# # draw worfklow graph downstream of SYNMAP_land_cover_map_data
# productName="SYNMAP_land_cover_map_data"
# $QUERIES_DIR/render_wf_graph_downstream_of_data_q3.sh \'$productName\' > $RESULTS_DIR/wf_downstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.svg

# # draw worfklow graph downstream of lat_variable
# productName="lat_variable"
# $QUERIES_DIR/render_wf_graph_downstream_of_data_q3.sh $productName > $RESULTS_DIR/wf_downstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.svg

# # draw worfklow graph downstream of Grass_variable
# productName="Grass_variable"
# $QUERIES_DIR/render_wf_graph_downstream_of_data_q3.sh \'$productName\' > $RESULTS_DIR/wf_downstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_downstream_of_$productName.gv > $RESULTS_DIR/wf_downstream_of_$productName.svg


# ##############
# #   Q4_pro   #
# ##############

# # list script outputs downstream of input data mean_airtemp
# productName="mean_airtemp"
# $QUERIES_DIR/list_outputs_downstream_of_data_q4.sh $productName $productName > $RESULTS_DIR/outputs_downstream_of_$productName.txt

# # list script outputs downstream of input data mean_precip
# productName="mean_precip"
# $QUERIES_DIR/list_outputs_downstream_of_data_q4.sh $productName $productName > $RESULTS_DIR/outputs_downstream_of_$productName.txt


# # list script outputs downstream of input data SYNMAP_land_cover_map_data
# productName="SYNMAP_land_cover_map_data"
# $QUERIES_DIR/list_outputs_downstream_of_data_q4.sh \'$productName\' $productName > $RESULTS_DIR/outputs_downstream_of_$productName.txt


# ##############
# #   Q5_pro   #
# ##############

# # draw recon worfklow graph upstream of C3_fraction_data
# productName="C3_fraction_data"
# $QUERIES_DIR/render_wf_recon_graph_upstream_of_data_q5.sh \'$productName\' > $RESULTS_DIR/wf_recon_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.svg


# # draw recon worfklow graph upstream of C4_fraction_data
# productName="C4_fraction_data"
# $QUERIES_DIR/render_wf_recon_graph_upstream_of_data_q5.sh \'$productName\' > $RESULTS_DIR/wf_recon_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.svg

# # draw recon worfklow graph upstream of Grass_fraction_data
# productName="Grass_fraction_data"
# $QUERIES_DIR/render_wf_recon_graph_upstream_of_data_q5.sh \'$productName\' > $RESULTS_DIR/wf_recon_upstream_of_$productName.gv
# dot -Tpdf $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.pdf
# dot -Tsvg $RESULTS_DIR/wf_recon_upstream_of_$productName.gv > $RESULTS_DIR/wf_recon_upstream_of_$productName.svg

# ##############
# #   Q6_pro   #
# ##############


# # draw recon workflow graph with all observables

# $QUERIES_DIR/render_recon_complete_wf_graph_q6.sh > $RESULTS_DIR/wf_recon_complete_graph_all_observables.gv
# dot -Tpdf $RESULTS_DIR/wf_recon_complete_graph_all_observables.gv > $RESULTS_DIR/wf_recon_complete_graph_all_observables.pdf
# dot -Tsvg $RESULTS_DIR/wf_recon_complete_graph_all_observables.gv > $RESULTS_DIR/wf_recon_complete_graph_all_observables.svg
