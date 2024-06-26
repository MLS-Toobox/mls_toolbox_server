from mls.orchestration import Orchestrator
from . DataAcquisition import DataAcquisition
from . DataPreProcessing import DataPreProcessing
from . DataTransformation import DataTransformation
from . Train import Train
from . Evaluation import Evaluation

def main():
	root = Orchestrator()
	data_acquisition = DataAcquisition(
	)
	
	data_pre_processing = DataPreProcessing(
		dataset = (data_acquisition, 'dataset'),
	)
	
	data_transformation = DataTransformation(
		data = (data_pre_processing, 'data'),
	)
	
	train = Train(
		features = (data_transformation, 'features_train'),
		truth = (data_transformation, 'truth_train'),
	)
	
	evaluation = Evaluation(
		model = (train, 'model'),
		features = (data_transformation, 'features_test'),
		truth = (data_transformation, 'truth_test'),
	)
	
	root.add([
		data_acquisition,
		data_pre_processing,
		data_transformation,
		train,
		evaluation
	])

	root.execute()
